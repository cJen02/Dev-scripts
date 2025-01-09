# SPI on Jetson – Using Jetson-IO

`sudo find /opt/nvidia/jetson-io/ -mindepth 1 -maxdepth 1 -type d -exec touch {}/__init__.py \;`

`sudo /opt/nvidia/jetson-io/jetson-io.py`

`sudo cat /sys/kernel/debug/tegra_pinctrl_reg | grep -i spi`

Ref:
- https://github.com/JetsonHacksNano/SPI-Playground
- https://jetsonhacks.com/2020/05/04/spi-on-jetson-using-jetson-io/
- 
