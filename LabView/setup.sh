
## First Install ni-labview-2024-community_24.3.2.49152-0+f0-ubuntu2004_all.deb
## And NI Linux Device Drivers Manually

sudo apt update
sudo apt install ni-labview-2024-community
sudo apt install ni-visa
sudo apt install ni-hwcfg-utility

group hcr-sim-pc
sudo gpasswd --add hcr-sim-pc dialout
sudo apt update
