# SPI on Jetson – Using Jetson-IO

`sudo find /opt/nvidia/jetson-io/ -mindepth 1 -maxdepth 1 -type d -exec touch {}/__init__.py \;`

`sudo /opt/nvidia/jetson-io/jetson-io.py`

`sudo cat /sys/kernel/debug/tegra_pinctrl_reg | grep -i spi`

`sudo modprobe spidev`

`wget https://raw.githubusercontent.com/torvalds/linux/v4.9/tools/spi/spidev_test.c`

`gcc -o spidev_test spidev_test.c`

`sudo ./spidev_test -D /dev/spidev0.0 -v -p "HelloWorld123456789abcdef"`

`sudo ./spidev_test -D /dev/spidev0.0 -s 10000000 -v`


Ref:
- https://github.com/JetsonHacksNano/SPI-Playground
- https://jetsonhacks.com/2020/05/04/spi-on-jetson-using-jetson-io/
- https://forums.developer.nvidia.com/t/jetson-nano-spi-bus-not-working/249482/10
- 
- https://forums.developer.nvidia.com/t/how-can-i-enable-spi-communication-on-jetson-nano-module/229228/6

