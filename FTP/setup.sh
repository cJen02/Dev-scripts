### Ref:- https://phoenixnap.com/kb/install-ftp-server-on-ubuntu-vsftpd


#  Install vsftpd Server on Ubuntu
sudo apt update
sudo apt install vsftpd

# Launch vsftpd
sudo systemctl start vsftpd
sudo systemctl enable vsftpd

# Backup Configuration Files
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf_default

# Create FTP User
sudo useradd -m [username]
sudo passwd [username]

# Configure Firewall to Allow FTP Traffic
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp

# Connect to the FTP Server
sudo ftp [system_name]

