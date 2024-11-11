import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open on bus 0, device 0

# SPI Configuration
spi.max_speed_hz = 500000  # Set SPI speed
spi.mode = 0  # SPI mode


# Loopback Test Function
def spi_loopback_test():
    test_data = [0x01, 0x02, 0x03, 0x04, 0x05]
    print(f"Sending data: {test_data}")
    response = spi.xfer2(test_data)  # Send data over SPI
    print(f"Received data: {response}")

    if response == test_data:
        return True
    else:
        # Detailed feedback on mismatch
        print("SPI loopback test failed. Details:")
        for i, (sent, received) in enumerate(zip(test_data, response)):
            if sent != received:
                print(f"Byte {i}: Sent {hex(sent)}, Received {hex(received)}")
        return False


# Run the test
if spi_loopback_test():
    print("SPI loopback test passed.")
else:
    print("SPI loopback test failed. Check mismatch details above.")

# Close SPI connection
spi.close()
