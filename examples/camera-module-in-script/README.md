# Using the Camera Module in a script

To use the Camera Module in a Python script, we use  ```camera.capture()``` for still photos, and ```camera.start_recording()``` for video.

This allows you to take pictures and videos as part of your own program, triggered by the PIR sensor, time of day or anything else you decide to code.

Below are some basic examples of simple script elements you can add to your code. See our [combined project code](https://github.com/ThePiHut/PIR-Camera-Case/tree/master/examples/pir-camera-code) for a full PIR-triggered camera project.
## Photo script
```python
#imports
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/photo1.jpg')
camera.stop_preview()
```
*Note: we add a 2-second delay here to allow the camera to adjust to the current lighting conditions before taking a photo.*

## Video script
```python
#imports
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/video1.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
```
*Note: we add a 3-second delay here to allow the camera to adjust to the current lighting conditions before taking a photo.*
