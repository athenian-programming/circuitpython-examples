import time

import board
import neopixel

def clear_pixels(p):
    for i in range(p.n):
        pixels[i] = (0, 0, 0)
    pixels.show()

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

while True:
    clear_pixels(pixels)

    for i in range(10):
        pixels[i] = (10, 0, 0)
        pixels.show()
        time.sleep(.1)
