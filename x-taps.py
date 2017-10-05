import time

import adafruit_lis3dh
import board
import busio
import neopixel


# This is derviced from: https://github.com/adafruit/Adafruit_CircuitPython_LIS3DH/blob/master/examples/spinner.py

def flash(c):
    pixels.fill((0, 0, 0))
    for i in range(3):
        pixels.fill(c)
        pixels.show()
        time.sleep(0.1)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.1)


# Accelerometer tap threshold.  Higher values mean you need to tap harder to start a spin.
TAP_THRESHOLD = 20

# Initialize NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

# Initialize accelerometer
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=25)

# Set accelerometer range.
lis3dh.range = adafruit_lis3dh.RANGE_16_G

# Enable single click detection, but use a custom CLICK_CFG register value
# to only detect clicks on the X axis (instead of all 3 X, Y, Z axes).
lis3dh.set_click(1, TAP_THRESHOLD, click_cfg=0x01)

flash((20, 0, 0))

while True:
    # Read the raw click detection register value and check if there was a click detected.
    clicksrc = lis3dh.read_click_raw()
    if clicksrc & 0b01000000 > 0:
        # Check if this was a positive or negative click event.
        if clicksrc == 0b1010001:  # Positive click
            flash((0, 0, 20))
        elif clicksrc == 0b1011001:  # Negative click
            flash((0, 20, 00))

    # Small delay to stay responsive but give time for interrupt processing.
    time.sleep(0.05)
