sudo apt install mosquitto mosquitto-clients
sudo systemctl status mosquito

sudo mosquitto_passwd -c /etc/mosquitto/passwd username
sudo nano /etc/mosquitto/conf.d/default.conf
# listener 1883
# password_file /etc/mosquitto/passwd

sudo systemctl restart mosquitto
