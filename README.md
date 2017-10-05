# CircuitPython Examples

CircuitPython examples for the [Adafruit Circuit Playground Express](https://www.adafruit.com/product/3333)  board.

## CircuitPython API

The CircuitPython API docs are [here](https://circuitpython.readthedocs.io/en/1.x/index.html).

## Ampy Utility

The [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview) utility
simplifies running and debugging python code on the Circuit Playground. One big advantage is it
allows you to see the *stdout* from python `print` statements.

    
## Neopixels

Example code is in [neopixels.py](./neopixels.py).

The neopixels package is described [here](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel).

Note: 0x100000 is equivalent to (0x10, 0, 0).s

## Circuit Playground Hardware

Example code is in [hardware.py](./hardware.py).

The hardware package is described [here](https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/c98e4ee469564732dbc26b5ec06802230213fd91)

Board properties available in python:
```python
circuit.switch
circuit.button_a
circuit.button_b
circuit.light
circuit.temperature
circuit.red_led
```

## Accelerator

Example code is in:
* [x-taps.py](./x-taps.py)
* [accel-data.py](./accel-data.py)

The hardware package is described [here](https://github.com/adafruit/Adafruit_CircuitPython_LIS3DH).

Additional LIS3DH info is [here](https://learn.adafruit.com/circuitpython-hardware-lis3dh-accelerometer/software).

A spinner example is [here](https://github.com/adafruit/Adafruit_CircuitPython_LIS3DH/blob/master/examples/spinner.py).