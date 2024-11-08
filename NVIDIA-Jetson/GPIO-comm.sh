
## install GPIO utils
sudo apt-get update
sudo apt-get -y install python3-pip
sudo pip3 install Jetson.GPIO

## install SPI utils
wget https://forums.developer.nvidia.com/uploads/short-url/pHU1lykUAqfxJqx3MMhPfxFY9hu.dtb -o nano-spi.dtb
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
