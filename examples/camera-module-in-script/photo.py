#imports
from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
time.sleep(2)
camera.capture('/home/pi/photo1.jpg')
camera.stop_preview()