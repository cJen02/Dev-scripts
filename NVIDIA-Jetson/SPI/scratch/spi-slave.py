import Jetson.GPIO as GPIO
import time

# Define GPIO pins for SPI
SCK_PIN = 11     # Serial Clock from Master
MISO_PIN = 13    # Master In Slave Out
MOSI_PIN = 15    # Master Out Slave In
SS_PIN = 16      # Slave Select from Master

# SPI Parameters
CLOCK_DELAY = 0.0001  # Short delay for stable clock detection (100 µs)
RESPONSE_CHAR = 'A'   # ASCII character to respond with

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SCK_PIN, GPIO.IN)         # SCK as input (driven by master)
    GPIO.setup(MOSI_PIN, GPIO.IN)        # MOSI as input (driven by master)
    GPIO.setup(MISO_PIN, GPIO.OUT, initial=GPIO.LOW)  # MISO as output (driven by slave)
    GPIO.setup(SS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # SS as input with pull-up

def spi_slave():
    print("Waiting for SPI communication...")
    try:
        while True:
            # Wait for SS (Slave Select) to go LOW (active)
            while GPIO.input(SS_PIN) == GPIO.HIGH:
                time.sleep(CLOCK_DELAY)

            print("Slave Select activated!")
            received_byte = 0
            bit_index = 7  # Start with the most significant bit
            response_byte = ord(RESPONSE_CHAR)  # Convert response char to byte

            while GPIO.input(SS_PIN) == GPIO.LOW:  # While SS is active
                # Wait for SCK to go HIGH (rising edge)
                while GPIO.input(SCK_PIN) == GPIO.LOW:
                    time.sleep(CLOCK_DELAY)

                # Read the bit from MOSI
                bit = GPIO.input(MOSI_PIN)
                received_byte |= (bit << bit_index)

                # Send the corresponding bit on MISO
                response_bit = (response_byte >> bit_index) & 0x01
                GPIO.output(MISO_PIN, response_bit)

                # Wait for SCK to go LOW (falling edge)
                while GPIO.input(SCK_PIN) == GPIO.HIGH:
                    time.sleep(CLOCK_DELAY)

                bit_index -= 1  # Move to the next bit

                if bit_index < 0:  # Byte transmission complete
                    # Convert received byte to ASCII char (if printable)
                    received_char = chr(received_byte) if 32 <= received_byte <= 126 else '?'
                    print(f"Received byte: 0x{received_byte:02X} ('{received_char}')", end="\t")
                    print(f"Responded with byte: 0x{response_byte:02X} ('{RESPONSE_CHAR}')")

                    # Reset for the next byte
                    received_byte = 0
                    bit_index = 7

    except KeyboardInterrupt:
        print("\nExiting SPI Slave...")
    finally:
        GPIO.cleanup()

# Main function
if __name__ == "__main__":
    setup_gpio()
    spi_slave()
