import time

import board
import neopixel

if __name__ == '__main__':
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

    while True:
        # Clear pixels
        pixels.fill((0, 0, 0))

        # Set pixel
        for i in range(10):
            pixels[i] = (10, 0, 0)
            pixels.show()
            time.sleep(.1)
