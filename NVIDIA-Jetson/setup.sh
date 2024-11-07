
## Python issues
sudo apt purge -y python2.7-minimal
sudo apt purge -y python3.6-minimal
sudo apt-get autoremove --purge
sudo apt install python3.8
sudo ln -s /usr/bin/python3.8 /usr/bin/python
sudo apt install -y python3-pip
sudo ln -s /usr/bin/pip3 /usr/bin/pip
python --version

## GPIO packages
sudo pip3 install Jetson.GPIO
sudo groupadd -f -r gpio
sudo usermod -a -G gpio {username}

## VNC setup - https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup
mkdir -p ~/.config/autostart
cp /usr/share/applications/vino-server.desktop ~/.config/autostart/.
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
Set a password to access the VNC server

# Replace thepassword with your desired password
gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n 'thepassword'|base64)
sudo

## Install VScode
VERSION=1.85.2
wget -N -O vscode-linux-deb.arm64.deb https://update.code.visualstudio.com/$VERSION/linux-deb-arm64/stable
sudo apt install ./vscode-linux-deb.arm64.deb


