import time

import adafruit_lis3dh
import board
import busio

# Initialize accelerometer
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=25)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G

i = 0
while True:
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y, z axis values.
    x, y, z = lis3dh.acceleration
    print('{} x = {}G, y = {}G, z = {}G'.format(i, x / 9.806, y / 9.806, z / 9.806))
    i = i + 1
    # Small delay to keep things responsive but give time for interrupt processing.
    time.sleep(0.25)
