import cv2
import numpy as np

import requests

URL = r"http://192.168.137.37:81/stream"

cap = cv2.VideoCapture(URL)

if __name__ == '__main__':
    
    while True:
        if cap.isOpened():
            ret, frame = cap.read()

            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)

                
            cv2.imshow("frame", frame)

            key = cv2.waitKey(1)

            if key == 27:
                break

            #elif key == ord('r'):
            #    idx = int(input("Select resolution index: "))
            #    set_resolution(URL, index=idx, verbose=True)

            #elif key == ord('q'):
            #    val = int(input("Set quality (10 - 63): "))
            #    set_quality(URL, value=val)

            #elif key == ord('a'):
            #    AWB = set_awb(URL, AWB)

            
    cv2.destroyAllWindows()
    cap.release()