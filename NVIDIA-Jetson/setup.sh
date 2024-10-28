
## Python issues
sudo apt purge -y python2.7-minimal
sudo apt purge -y python3.6-minimal
sudo apt install python3.8
sudo ln -s /usr/bin/python3.8 /usr/bin/python
sudo apt install -y python3-pip
sudo ln -s /usr/bin/pip3 /usr/bin/pip
python --version

## GPIO packages
sudo pip3 install Jetson.GPIO
sudo groupadd -f -r gpio
sudo usermod -a -G gpio {username}


## Install VScode
VERSION=1.94.2
wget -N -O vscode-linux-deb.arm64.deb https://update.code.visualstudio.com/$VERSION/linux-deb-arm64/stable
sudo apt install ./vscode-linux-deb.arm64.deb


