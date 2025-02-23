sudo apt-get update 
sudo apt-get upgrade -y

# sudo apt-get install -y docker.io
docker --verison

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

sudo apt-get install -y nano
sudo nano /etc/docker/daemon.json

# {
# "runtimes": {
#     "nvidia": {
#         "path": "nvidia-container-runtime",
#         "runtimeArgs": []
#     }
# },
# "default-runtime": "nvidia"
# }

sudo systemctl restart docker
docker info | grep -i runtime
# Runtimes: nvidia runc
# Default Runtime: nvidia

