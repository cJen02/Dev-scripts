# Linux UFW services
sudo apt-get install ufw
sudo systemctl enable ufw
sudo systemctl start ufw
sudo ufw reset

sudo ufw default allow incoming
sudo ufw default allow outgoing
sudo ufw status
