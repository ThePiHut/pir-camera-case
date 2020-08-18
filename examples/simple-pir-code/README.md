# Simple PIR Code

Here is some simple code to test your PIR module and give you an idea of the range and sensitivity of the module. You can also use this (or parts of it) for your own custom script.

In this example we've wired up the PIR module to the Raspberry Pi's 5V, GND and GPIO 17 (physical pin 11) pins as per the [assembly guide](https://github.com/ThePiHut/PIR-Camera-Case).

The code looks for input from the PIR module, which will give a signal via GPIO 17 when it detects motion.

```python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

try:
	print("PIR Module Test (CTRL+C to exit)")
	time.sleep(2)
	print("Ready")
	while True:
		if GPIO.input(PIR_PIN):
			print("Motion Detected!")
		time.sleep(1)

except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
```
