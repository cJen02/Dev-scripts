import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open bus 0, device 0
spi.max_speed_hz = 500000  # 500 kHz
spi.mode = 0b00  # SPI mode 0

def loopback_test():
    test_data = [0x01, 0x02, 0x03, 0x04, 0x05]
    print(f"Sending: {test_data}")
    
    # Send and receive data
    received_data = spi.xfer2(test_data)
    print(f"Received: {received_data}")
    
    if test_data == received_data:
        print("Loopback Test Passed!")
    else:
        print("Loopback Test Failed!")

try:
    while True:
        loopback_test()
        time.sleep(1)
except KeyboardInterrupt:
    spi.close()
    print("SPI communication closed.")
