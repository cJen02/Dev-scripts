

# nano ~/.bashrc
# # export PATH=/usr/local/cuda/bin:$PATH
# # export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
# source ~/.bashrc

nvcc --version

# Test running a basic NVIDIA container
sudo docker run --rm --runtime=nvidia --gpus all nvcr.io/nvidia/l4t-base:r35.2.1 bash -c "echo GPU is accessible"

# Now setup the ML image of dusty-nv provided by nvidia zoo
sudo docker run --rm --runtime=nvidia --gpus all -it -p 8888:8888 nvcr.io/nvidia/l4t-ml:r35.2.1-py3

# Persist Data with a Mounted Volume To save files after stopping the container:
sudo docker run --runtime=nvidia --gpus all -it -v ~/ml_workspace:/workspace nvcr.io/nvidia/l4t-ml:r35.2.1-py3


# Install VSCode for code support
git clone https://github.com/JetsonHacksNano/install/VSCode.git
cd installVSCode
./installVSCode.sh

# Setup jtop to Check GPU, CPU Usage in Jetson Nano
sudo apt install python3-pip -y
sudo pip3 install jetson-stats
jtop # to run jtop
