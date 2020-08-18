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
	print "Ready"

	while True:
		if GPIO.input(PIR_PIN):

			print "Motion Detected!"

			timestamp = time.strftime("%Y%m%d-%H%M%S")
			video_name = 'VID_' + timestamp + '.h264'

			camera.start_recording(video_name)
			time.sleep(10)
			camera.stop_recording()
			camera.stop_preview()

			time.sleep(2)
			print "Ready"

		time.sleep(1)

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()