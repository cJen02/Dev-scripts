import Jetson.GPIO as GPIO
import spidev
import time

# SPI Bus and Device
SPI_BUS = 0
SPI_DEVICE = 0

# GPIO pin for Chip Select (SS)
SS_PIN = 15

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Configure SS as input

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 50000  # Match the master's speed
spi.mode = 0b00  # SPI mode (CPOL=0, CPHA=0)

# Data to respond to the master
slave_response = 0x37  # Example response byte

def listen_spi_slave():
    print("Waiting for SPI communication...")
    try:
        while True:
            # Check if SS is active (LOW)
            if GPIO.input(SS_PIN) == GPIO.LOW:
                print("Slave Select activated!")

                # Wait for data from master
                received_data = spi.readbytes(1)  # Read 1 byte from master
                print(f"Received from Master: 
