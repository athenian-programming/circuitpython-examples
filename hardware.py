from adafruit_circuitplayground.express import circuit

while True:
    if circuit.button_a:
        print("Temperature:", circuit.temperature)
    circuit.red_led = circuit.button_b
