# Basic Camera Module Commands

Here are some simple camera commands you can run from a terminal window once you have your case assembled and the [camera enabled](https://github.com/ThePiHut/PIR-Camera-Case#prepare-your-raspberry-pi).

## Photos

**Take a simple photo**
```bash
raspistill -o yourphoto.jpg
```
**Flip the photo horizontally**
```bash
raspistill -hf -o yourphoto.jpg
```
**Flip the photo vertically**
```bash
raspistill -vf -o yourphoto.jpg
```
**Flip the photo upside down (combine the flips)**
```bash
raspistill -vf -hf -o yourphoto.jpg
```
## Video

**Record a default 5-second video**
```bash
raspivid -o testvideo.h264
```

**Record a 20-second video**
```bash
raspivid -o testvideo.h264 -t 20000
```
**Flip a 30-second video horizontally**
```bash
raspivid -hf -o testvideo.h264 -t 30000
```
**Flip a 60-second video vertically**
```bash
raspivid -vf -o testvideo.h264 -t 60000
```
**Flip a 25-second video upside down (combine the flips)**
```bash
raspivid -vf -hf -o testvideo.h264 -t 25000
```
