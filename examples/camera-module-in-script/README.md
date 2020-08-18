# Using the Camera Module in a script

To use the Camera Module in a Python script, we use  ```camera.capture()``` for still photos, and ```camera.start_recording()``` for video.

This allows you to take pictures and videos as part of your own program, triggered by the PIR sensor, time of day or anything else you decide to code.

Below are some examples of simple script elements you can add to your code. See our **combined project code** for a full PIR-triggered camera project.
## Photo script
```python
#imports
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/photo1.jpg')
camera.stop_preview()
```
*Note: we add a 3-second delay here to allow the camera to adjust to the current lighting conditions before taking a photo.*

## Video script
```python
#imports
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/Desktop/video1.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
```
*Note: we add a 3-second delay here to allow the camera to adjust to the current lighting conditions before taking a photo.*

## Date-based filenames
These code examples are a good start, however you may not want to constantly overwrite the same image/video file.

You can create your files by adding this import:
```python
from datetime import datetime 
```
Then change the capture line to the following **for photos:**
```python
camera.capture('/home/pi/Desktop/{timestamp:%Y-%m-%d-%H-%M-%S}.jpg')
```
Or change the capture line to this **for videos**:
```python
camera.start_recording('/home/pi/Desktop/{timestamp:%Y-%m-%d-%H-%M-%S}.jpg')
```
