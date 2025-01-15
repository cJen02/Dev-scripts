import Jetson.GPIO as GPIO
import spidev
import time

# SPI Configuration
SPI_BUS = 0            # SPI bus (usually 0 on Jetson Nano)
SPI_DEVICE = 0         # SPI device (usually 0 on Jetson Nano)
SS_PIN = 15            # Chip Select (Slave Select) pin
SPI_SPEED = 50000      # SPI communication speed in Hz
SPI_MODE = 0b00        # SPI mode (CPOL=0, CPHA=0)

# Initialize SPI and GPIO
def setup():
    # Set up GPIO for SS pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # SS as input with pull-up
    
    # Initialize SPI
    spi = spidev.SpiDev()
    spi.open(SPI_BUS, SPI_DEVICE)
    spi.max_speed_hz = SPI_SPEED
    spi.mode = SPI_MODE
    return spi

# Function to listen for SPI communication
def listen_spi_slave(spi):
    print("Waiting for SPI communication...")
    slave_response = 0x37  # Example response byte

    try:
        while True:
            # Check if SS (Slave Select) is active (LOW)
            if GPIO.input(SS_PIN) == GPIO.LOW:
                print("Slave Select activated!")

                # Wait for data from the master
                received_data = spi.readbytes(1)  # Read 1 byte from master
                print(f"Received from Master: {received_data[0]:#04x}")

                # Send a response to the master
                spi.writebytes([slave_response])
                print(f"Sent to Master: {slave_response:#04x}")

                # Wait for SS to go HIGH again (end of transaction)
                while GPIO.input(SS_PIN) == GPIO.LOW:
                    time.sleep(0.001)  # Small delay to reduce CPU usage

    except KeyboardInterrupt:
        print("\nExiting SPI Slave...")
    finally:
        spi.close()
        GPIO.cleanup()

# Main function
if __name__ == "__main__":
    spi = setup()
    listen_spi_slave(spi)
