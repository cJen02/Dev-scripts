"""
### MQTT Web-cam publish.py

- capture webcam image using OpenCV
- save image to IO.Stream
- convert to bytearray & publish to "c340/webcam"
"""

import paho.mqtt.client as mqtt
import cv2 
import io
import base64
import re

import time
from datetime import datetime as dt

from pylab import *

PATH = "D:/Database/cam1/230513/"

SERVER = "192.168.137.1"
TOPIC = "Sys/C340"

cam_port = 0
CAM_URL = r"http://192.168.137.37:81/stream"

cam = cv2.VideoCapture(CAM_URL)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
frames = 30
delay_sec = 0

client = mqtt.Client()
client.connect(SERVER)

stream = io.BytesIO()

def encode_time(h=None, m=None, s=None, f=None):
    time = dt.now()
    if not h: h=time.hour
    if not m: m=time.minute
    if not s: s=time.second
    if not f: f=time.microsecond

    h = "0"+str(h) if h<10 else h
    m = "0"+str(m) if m<10 else m
    s = "0"+str(s) if s<10 else s
    f = "0"+str(f) if f<10 else f
    return f"{h}{m}{s}-{f}"

def encode_date(sp=''):
    date = dt.now().date()
    year = date.year
    month = "0"+str(date.month) if date.month<10 else date.month
    day = "0"+str(date.day) if date.day<10 else date.day
    return f"{year}{sp}{month}{sp}{day}"

def encode_datetime():
    return f"{encode_date()}-{encode_time()}"

def capture_and_show():
    ret, frame = cam.read()

    if ret:
        cv2.imwrite("image.png", frame)
        
        cv2.imshow(f"Cam-{cam_port}", frame)
        cv2.waitKey(0)
        cv2.destroyWindow(f"Cam-{cam_port}")
      
    else:
        print("No image detected. Please! try again")

def mqtt_capture_publish(delay_sec):
    start = time.time()

    for i in range(frames):
        ret, frame = cam.read()

        if ret:
            cv2.imwrite(f"{PATH}{encode_datetime()}.png", frame)

            _, buffer = cv2.imencode('.jpg', frame)
            #byteArr = base64.b64encode(buffer)
            stream = buffer.tobytes()
            
            #cv2.imwrite("buffer.jpg", frame)
            #with open("buffer.jpg", "rb") as f: stream = f.read()

            byteArr = bytearray(stream)
            client.publish(f"{TOPIC}/Image", byteArr)

            #stream.seek(0)
            #stream.truncate()
        time.sleep(delay_sec)
        
    end = time.time()
    t = end - start
    fps = round(frames/t, 2)
    
    client.publish(f"{TOPIC}/Frame", fps)
    print(fps, delay_sec)

    return fps

    
##################################################
   
#capture_and_show()
#input("press ENTER to exit...")

client.publish(TOPIC, "Online")

delay_sec = 0
while True:
    fps = mqtt_capture_publish(delay_sec)
    
    if (fps<10): delay_sec -= 0.01
    if (fps>12): delay_sec += +0.01
    if (delay_sec<0): delay_sec = 0