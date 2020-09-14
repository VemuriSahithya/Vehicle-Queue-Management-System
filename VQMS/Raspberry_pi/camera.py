import RPi.GPIO as GPIO
import time
from time import sleep
import os

def camera():
    print("Taking a pic!")
    os.system('fswebcam -p YUYV -d /dev/video0 -r 640x480 --no-banner /home/pi/Desktop/image.jpg > output_pic.txt')
    print("Photo Taken")
    return