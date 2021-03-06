# Raspberry Pi PIR Camera Case

*Repository containing setup, code and Python script examples for the Raspberry Pi PIR Camera Case from The Pi Hut*
***
The PIR Camera Case ([Pi 4](https://thepihut.com/products/pir-camera-case-for-raspberry-pi-4-3) / Pi Zero *(Coming soon)*) is a case designed to hold your Raspberry Pi, an Official Raspberry Pi Camera Module and the included PIR sensor. The case is also compatible with [these wall mounts](https://thepihut.com/products/camera-box-wall-mount).

When used together, you have a great foundation for an indoors Raspberry Pi motion-sensing camera project. Combine with [MotionEyeOS](https://github.com/ccrisan/motioneyeos/wiki) for a superb Raspberry Pi IP surveillance system!

![PIR Camera Case](/images/PIR-Camera-Case-2.jpg)

This repository will show you how to [prepare your Raspberry Pi](#prepare-your-raspberry-pi), give you some [example code](#example-code) to get you started (including how to [download this code straight to your Raspberry Pi](#downloading-example-code)).

## Prepare your Raspberry Pi

**Operating System**

We recommend the [Raspberry Pi OS](https://www.raspberrypi.org/downloads/) for this project/case, and this guide assumes you have the basic operating system loaded and ready.
You can also use other systems such as [MotionEyeOS](https://github.com/ccrisan/motioneyeos/wiki) for a live video surveillance style system.

**Case Assembly**

You will need to have [assembled the case](https://thepihut.com/blogs/raspberry-pi-tutorials/pir-camera-case-assembly-instructions) which includes connecting the Camera Module and PIR sensor.

**Enable the Camera Interface**

We need to make sure your Raspberry Pi is configured to use the Camera Module to enable it to take photos/videos when instructed by our code.

We will enable the camera interface by opening a new terminal window and entering:
```bash
sudo raspi-config
```
This will show a screen similar to this:

![Raspi-Config](images/raspi-config-screen.jpg)

Now simply select '**Interfacing Options**', '**Camera**' then '**Yes**' to enable the camera interface. Reboot your Raspberry Pi when prompted.

**Test the Camera**

Run a quick test before proceeding. With your Raspberry Pi connected to a monitor via a HDMI cable, in a terminal window enter the following command to take a quick basic picture with the camera:
```bash
raspistill -o test.jpg
```
If you don't see an image on the screen, check the camera connection, re-fit the cable if necessary, reboot and try again.

**Adjust PIR sensitivity**

PIR modules are usually set to half sensitivity out of the bag via the right-hand dial seen in the image below:

![PIR Sensitivity](https://github.com/ThePiHut/pir-camera-case/blob/master/images/PIR-settings.jpg)

This can be a little too sensitive depending on the conditions your project will be in. If you experience excessive false triggers, open the top of your case and try turning the right dial anti-clockwise and testing different levels of sensitivity. Heat, WiFi and other interference can also produce false triggers

## Example Code

We have added examples below showing you how to control the individual components, alongside a combined code example showing a full motion-sensing camera project.

Remember: PIR sensors can be temperamental (and can be impacted by WiFi, heat and other interference) so will need some [tweaking](https://github.com) to avoid excessive false triggers.

**Controlling individual components**
- [Simple PIR code](https://github.com/ThePiHut/pir-camera-case/tree/master/examples/simple-pir-code)
- [Basic camera module terminal commands](https://github.com/ThePiHut/pir-camera-case/tree/master/examples/basic-camera-commands)
- [Using the camera module in a script](https://github.com/ThePiHut/pir-camera-case/tree/master/examples/camera-module-in-script)

**Motion sensing project example**
- [PIR + Camera code](https://github.com/ThePiHut/pir-camera-case/tree/master/examples/pir-camera-code)

## Downloading example code
You can download this entire repository on to your Raspberry Pi (including the example scripts) by following the steps below:

In a terminal window, enter the following command:

```git clone https://github.com/ThePiHut/pir-camera-case```

To enter the cloned repository directory, use:

```cd pir-camera-case```

You can then access the example scripts by finding them in their respective directories. For example:

```cd examples/pir-camera-code```

If you then use the command ```ls``` to list the contents of that directory, you'll see the code file. You can then, for example, run that file with:

```sudo python videoproject.py```
