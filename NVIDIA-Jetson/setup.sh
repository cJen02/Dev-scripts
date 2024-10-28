
# Python issues
sudo apt purge -y python2.7-minimal
sudo apt purge -y python3.6-minimal
sudo apt install python3.8
sudo ln -s /usr/bin/python3.8 /usr/bin/python
sudo apt install -y python3-pip
sudo ln -s /usr/bin/pip3 /usr/bin/pip
python --version


## Install VScode
git clone https://github.com/JetsonHacksNano/installVSCode.git
cd installVSCode
./installVSCode.sh

