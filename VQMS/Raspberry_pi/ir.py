import RPi.GPIO as GPIO
import time
from time import sleep
import os

def IR1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.IN)
    sensor=GPIO.input(27)
    if(sensor==1):
        ret= 1
    else:
        ret=0
    return ret

def IR0():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.IN)
    print("Waiting for the car to leave")
    while True:
        sensor=GPIO.input(27)
        if(sensor==0):
            return 1
    return 1        
