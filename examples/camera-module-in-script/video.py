#imports
from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/video1.h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()