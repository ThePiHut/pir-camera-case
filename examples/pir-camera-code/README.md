# PIR + Camera code

The examples below can be used as a foundation for your own project, where you can add more advanced functions and features if you decide to.

Our example projects combine the [PIR example](https://github.com/ThePiHut/pir-camera-case/tree/master/examples/simple-pir-code) and [Camera Module script examples](https://github.com/ThePiHut/pir-camera-case/tree/master/examples/camera-module-in-script) into a single project - taking a photo or video every time motion is detected.

Rememeber that PIR sensors can be temperamental (*and can be impacted by WiFi, heat and other interference*) so will need some [tweaking](https://github.com/ThePiHut/pir-camera-case#prepare-your-raspberry-pi) to avoid excessive false triggers.
## Video Project
This project takes a 10-second video every time motion is detected by the PIR sensor. 

We've added a timestamp feature to give each video a unique filename (to avoid re-writing over the same one each time).
```python
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from datetime import datetime 

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

camera = PiCamera()

try:
	time.sleep(5)
	print("Ready")

	while True:
		if GPIO.input(PIR_PIN):
			
			print("Motion Detected!")
			
			timestamp = time.strftime("%Y%m%d-%H%M%S")
			video_name = 'VID_' + timestamp + '.h264'

			camera.start_recording(video_name)
			time.sleep(10)
			camera.stop_recording()
			camera.stop_preview()

			time.sleep(2)
			print("Ready")

		time.sleep(1)

except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
```
## Photo Project
This project is similar to the video project example above but instead takes a picture every time motion is detected by the PIR sensor.
```python
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from datetime import datetime 

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

camera = PiCamera()

try:
	time.sleep(5)
	print("Ready")

	while True:
		if GPIO.input(PIR_PIN):
			
			print("Motion Detected!")
			
			timestamp = time.strftime("%Y%m%d-%H%M%S")
			image_name = 'IMG_' + timestamp + '.jpg'

			camera.start_preview()
			time.sleep(2)
			camera.capture(image_name)
			camera.stop_preview()

			time.sleep(2)
			print("Ready")

		time.sleep(1)

except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
```
*Note: we add a 2-second delay after* ```camera.start_preview()``` *to allow the camera to adjust to the current lighting conditions before taking a photo.*
