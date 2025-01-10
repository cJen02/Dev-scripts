#!/usr/bin/python3

import spidev
import time
import binascii

spi = spidev.SpiDev() # Tạo đối tượng cho SPI
spi.open(0, 0) # mở port 0, device (CS) 0
#spi.open(1, 0) # mở port 0, device (CS) 0
spi.max_speed_hz = 500000
#spi.max_speed_hz = 11000000

try:
  while True:
    print("abc")
    resp = spi.xfer2([0x61,0x62,0x63,0xA]) # [‘a’,‘b’,‘c’,‘\n’]
    time.sleep(1) # sleep for 1 seconds
except KeyboardInterrupt:
  spi.close()
