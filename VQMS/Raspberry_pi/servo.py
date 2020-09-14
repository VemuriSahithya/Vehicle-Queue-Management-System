import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
control = [3, 8]

servo = 17

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo,GPIO.OUT)
	p=GPIO.PWM(servo,50)# 50hz frequency
	p.start(0)# starting duty cycle ( it set the servo to 0 degree )
	print("hi")
	return p

def endProgram():
	GPIO.cleanup()
	return

def openDoor():
	try:
		p=setup()
		#p.ChangeDutyCycle(10)
		for x in range(1):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.5)
			print (control[x])
	finally:
		endProgram()
	return

def closeDoor():
	try:
		p=setup()
		#p.ChangeDutyCycle(10)
		for x in range(1,2):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.5)
			print (control[x])
	finally:
		endProgram()
	return
    
num_match=0

#if(num_match==1):
openDoor()
time.sleep(2)
closeDoor()
#elif()
print("information mismatch")
