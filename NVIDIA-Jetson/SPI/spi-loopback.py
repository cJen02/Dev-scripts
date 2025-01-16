import Jetson.GPIO as GPIO
import time

# Define GPIO pins for SPI
SCK_PIN = 11     # Serial Clock
MOSI_PIN = 13    # Master Out Slave In
MISO_PIN = 15    # Master In Slave Out
SS_PIN = 16      # Slave Select

# SPI Parameters
CLOCK_DELAY = 0.001  # Clock pulse width in seconds (1ms)

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SCK_PIN, GPIO.OUT, initial=GPIO.LOW)  # Clock
    GPIO.setup(MOSI_PIN, GPIO.OUT, initial=GPIO.LOW)  # MOSI
    GPIO.setup(MISO_PIN, GPIO.IN)                    # MISO
    GPIO.setup(SS_PIN, GPIO.OUT, initial=GPIO.HIGH)  # SS

def spi_transfer_byte(data_out):
    """Manually transfer a byte over SPI and return received byte."""
    data_in = 0

    # Pull SS low to start communication
    GPIO.output(SS_PIN, GPIO.LOW)

    for i in range(8):  # SPI is an 8-bit protocol
        # Write MOSI (Most Significant Bit first)
        bit_out = (data_out & (1 << (7 - i))) != 0
        GPIO.output(MOSI_PIN, GPIO.HIGH if bit_out else GPIO.LOW)

        # Pulse SCK (Clock) high
        GPIO.output(SCK_PIN, GPIO.HIGH)
        time.sleep(CLOCK_DELAY)

        # Read MISO (data from slave)
        bit_in = GPIO.input(MISO_PIN)
        data_in = (data_in << 1) | bit_in

        # Pulse SCK (Clock) low
        GPIO.output(SCK_PIN, GPIO.LOW)
        time.sleep(CLOCK_DELAY)

    # Pull SS high to end communication
    GPIO.output(SS_PIN, GPIO.HIGH)

    return data_in

def loopback_test():
    """Perform a loopback test by connecting MOSI to MISO."""
    print("Starting SPI loopback test...")
    try:
        for byte_out in range(256):  # Test all byte values from 0x00 to 0xFF
            received_byte = spi_transfer_byte(byte_out)
            print(f"Sent: 0x{byte_out:02X}, Received: 0x{received_byte:02X}")

            # Check if the loopback worked
            if byte_out != received_byte:
                print(f"Error: Mismatch on byte 0x{byte_out:02X}")
                break
        else:
            print("Loopback test successful!")

    except KeyboardInterrupt:
        print("\nExiting test...")
    finally:
        GPIO.cleanup()

# Main Function
if __name__ == "__main__":
    setup_gpio()
    loopback_test()
