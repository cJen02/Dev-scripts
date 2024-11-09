
## install GPIO utils
sudo apt-get update
sudo apt-get -y install python3-pip
sudo pip3 install Jetson.GPIO

## install SPI utils
wget -O nano-spi.dtb https://forums.developer.nvidia.com/uploads/short-url/pHU1lykUAqfxJqx3MMhPfxFY9hu.dtb
sudo cp nano-spi.dtb /boot/

sudo apt-get install nano
sudo nano /boot/extlinux/extlinux.conf

"""
And a paste below line to extlinux.conf file :

LABEL JetsonIO
MENU LABEL Custom Header Config: <HDR40 User Custom [2022-09-29-210441]>
LINUX /boot/Image
FDT /boot/nano-spi.dtb
INITRD /boot/initrd
APPEND ${cbootargs} quiet root=/dev/mmcblk0p1 rw rootwait rootfstype=ext4 console=ttyS0,115200n8 console=tty0 fbcon=map:0 net.ifnames=0
"""

## install py-spidev library
sudo apt-get install python-dev
sudo apt-get install python3-dev
git clone https://github.com/doceme/py-spidev.git
cd py-spidev
sudo apt-get install -y python-setuptools
sudo python setup.py install
sudo python3 setup.py install
sudo modprobe spidev # Load the spidev driver by below command first

"""
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
"""


## Load SPI drivers if needed
sudo modprobe spidev


### Jetson Nano SPI slave

"""
Edit in the dts file as the following - https://forums.developer.nvidia.com/t/spi-slave-for-l4t-r28-1/55401#5221958
>>> compatible = "nvidia,tegra210-spi"; 

"""
