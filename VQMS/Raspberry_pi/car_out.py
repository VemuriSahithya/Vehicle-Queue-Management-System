import RPi.GPIO as GPIO
import time
from time import sleep
import os
#-------------------------------servocode--------------------------

control = [3, 8]

servo = 17

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo,GPIO.OUT)
	p=GPIO.PWM(servo,50)# 50hz frequency
	p.start(0)# starting duty cycle ( it set the servo to 0 degree )
	#print("hi")
	return p

def endProgram():
	return

def openDoor():
	try:
		p=setup()
		#p.ChangeDutyCycle(10)
		for x in range(1):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.5)
			#print (control[x])
	finally:
            endProgram()
		#do nothing
	return

def closeDoor():
	try:
		p=setup()
		#p.ChangeDutyCycle(10)
		for x in range(1,2):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.5)
			#print (control[x])
	finally:
            endProgram()
		#do nothing
	return
    
num_match=0
#-------------------------------------servocode---------------------------------

#-----------------------------Display Code---------------------------------
import time

import Adafruit_CharLCD as LCD


# Raspberry Pi pin configuration:


lcd_message1="Welcome To"
lcd_message2="IIT Guwahati"


def display():
    GPIO.setmode(GPIO.BCM)
    lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 5
    lcd_d4        = 6
    lcd_d5        = 12
    lcd_d6        = 13
    lcd_d7        = 26
    lcd_backlight = 4

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 20
    lcd_rows    = 2
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

    lcd.set_backlight(0)
    time.sleep(2.0)
    # Change message.
    lcd.clear()
    lcd.message(lcd_message1)
    lcd.message('\n')
    lcd.message(lcd_message2)
    
    # Turn backlight on.
    lcd.set_backlight(1)
 
lcd_message1="Thank You"
lcd_message2="Visit Again" 
def display1():
    GPIO.setmode(GPIO.BCM)
    lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 5
    lcd_d4        = 6
    lcd_d5        = 12
    lcd_d6        = 13
    lcd_d7        = 26
    lcd_backlight = 4

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 20
    lcd_rows    = 2
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

    lcd.set_backlight(0)
    time.sleep(2.0)
    # Change message.
    lcd.clear()
    lcd.message(lcd_message11)
    lcd.message('\n')
    lcd.message(lcd_message21)
    
    # Turn backlight on.
    lcd.set_backlight(1)
    
lcd_message12="Request Not Found"
lcd_message22="----Error----"
def display2():
    GPIO.setmode(GPIO.BCM)
    lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 5
    lcd_d4        = 6
    lcd_d5        = 12
    lcd_d6        = 13
    lcd_d7        = 26
    lcd_backlight = 4

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 20
    lcd_rows    = 2
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

    lcd.set_backlight(0)
    time.sleep(2.0)
    # Change message.
    lcd.clear()
    lcd.message(lcd_message12)
    lcd.message('\n')
    lcd.message(lcd_message22)
    
    # Turn backlight on.
    lcd.set_backlight(1)
lcd_message13="Details Entered"
lcd_message23="Opening Gate"
def display3():
    GPIO.setmode(GPIO.BCM)
    lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 5
    lcd_d4        = 6
    lcd_d5        = 12
    lcd_d6        = 13
    lcd_d7        = 26
    lcd_backlight = 4

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 20
    lcd_rows    = 2
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

    lcd.set_backlight(0)
    time.sleep(2.0)
    # Change message.
    lcd.clear()
    lcd.message(lcd_message13)
    lcd.message('\n')
    lcd.message(lcd_message23)
    
    # Turn backlight on.
    lcd.set_backlight(1)
    
lcd_message14="Accepted Request"
lcd_message24="Opening Gate"
def display4():
    GPIO.setmode(GPIO.BCM)
    lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 5
    lcd_d4        = 6
    lcd_d5        = 12
    lcd_d6        = 13
    lcd_d7        = 26
    lcd_backlight = 4

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 20
    lcd_rows    = 2
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

    lcd.set_backlight(0)
    time.sleep(2.0)
    # Change message.
    lcd.clear()
    lcd.message(lcd_message14)
    lcd.message('\n')
    lcd.message(lcd_message24)
    
    # Turn backlight on.
    lcd.set_backlight(1)
#-----------------------------Display code----------------------------------

#-------------------------------------IR Code---------------------------------
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
#-------------------------------------IR Code-----------------------------------

#------------------------------------Buzzer Code-----------------------------
def init_buzzer():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print('Buzzer program')
    buzzer = 21
    GPIO.setup(buzzer,GPIO.OUT)
    delay = 0.25
    for i in range(6):
        GPIO.output(buzzer,True)
         #print("on")
        time.sleep(delay)
        GPIO.output(buzzer,False)
             #print("off")
        time.sleep(delay)
             #time.sleep(5*delay)
    #except KeyboardInterrupt:
    
    return

def barricade_error():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print('Buzzer program')
    buzzer = 21
    GPIO.setup(buzzer,GPIO.OUT)
    delay = 0.25
    for i in range(1):
        GPIO.output(buzzer,True)
            #print("on")
        time.sleep(2*delay)
        GPIO.output(buzzer,False)
            #print("off")
        time.sleep(delay)
            #time.sleep(5*dela
    return

buzzer_pin=21
notes = {
	'B0' : 31,
	'C1' : 33, 'CS1' : 35,
	'D1' : 37, 'DS1' : 39,
	'EB1' : 39,
	'E1' : 41,
	'F1' : 44, 'FS1' : 46,
	'G1' : 49, 'GS1' : 52,
	'A1' : 55, 'AS1' : 58,
	'BB1' : 58,
	'B1' : 62,
	'C2' : 65, 'CS2' : 69,
	'D2' : 73, 'DS2' : 78,
	'EB2' : 78,
	'E2' : 82,
	'F2' : 87, 'FS2' : 93,
	'G2' : 98, 'GS2' : 104,
	'A2' : 110, 'AS2' : 117,
	'BB2' : 123,
	'B2' : 123,
	'C3' : 131, 'CS3' : 139,
	'D3' : 147, 'DS3' : 156,
	'EB3' : 156,
	'E3' : 165,
	'F3' : 175, 'FS3' : 185,
	'G3' : 196, 'GS3' : 208,
	'A3' : 220, 'AS3' : 233,
	'BB3' : 233,
	'B3' : 247,
	'C4' : 262, 'CS4' : 277,
	'D4' : 294, 'DS4' : 311,
	'EB4' : 311,
	'E4' : 330,
	'F4' : 349, 'FS4' : 370,
	'G4' : 392, 'GS4' : 415,
	'A4' : 440, 'AS4' : 466,
	'BB4' : 466,
	'B4' : 494,
	'C5' : 523, 'CS5' : 554,
	'D5' : 587, 'DS5' : 622,
	'EB5' : 622,
	'E5' : 659,
	'F5' : 698, 'FS5' : 740,
	'G5' : 784, 'GS5' : 831,
	'A5' : 880, 'AS5' : 932,
	'BB5' : 932,
	'B5' : 988,
	'C6' : 1047, 'CS6' : 1109,
	'D6' : 1175, 'DS6' : 1245,
	'EB6' : 1245,
	'E6' : 1319,
	'F6' : 1397, 'FS6' : 1480,
	'G6' : 1568, 'GS6' : 1661,
	'A6' : 1760, 'AS6' : 1865,
	'BB6' : 1865,
	'B6' : 1976,
	'C7' : 2093, 'CS7' : 2217,
	'D7' : 2349, 'DS7' : 2489,
	'EB7' : 2489,
	'E7' : 2637,
	'F7' : 2794, 'FS7' : 2960,
	'G7' : 3136, 'GS7' : 3322,
	'A7' : 3520, 'AS7' : 3729,
	'BB7' : 3729,
	'B7' : 3951,
	'C8' : 4186, 'CS8' : 4435,
	'D8' : 4699, 'DS8' : 4978
}



melody = [
  notes['E7'], notes['E7'], 0, notes['E7'],
  0, notes['C7'], notes['E7'], 0,
  notes['G7'], 0, 0,  0,
  notes['G6'], 0, 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0
]
tempo = [
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
]

def buzz(frequency, length):	 #create the function "buzz" and feed it the pitch and duration)

	if(frequency==0):
		time.sleep(length)
		return
	period = 1.0 / frequency 		 #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
	delayValue = period / 2		 #calcuate the time for half of the wave
	numCycles = int(length * frequency)	 #the number of waves to produce is the duration times the frequency
	
	for i in range(numCycles):		#start a loop from 0 to the variable "cycles" calculated above
		GPIO.output(buzzer_pin, True)	 #set pin 27 to high
		time.sleep(delayValue)		#wait with pin 27 high
		GPIO.output(buzzer_pin, False)		#set pin 27 to low
		time.sleep(delayValue)		#wait with pin 27 low
		
		
def play(melody,tempo,pause,pace):
	
	for i in range(0, len(melody)/2):		# Play song
		
		noteDuration = pace/tempo[i]
		buzz(melody[i],noteDuration)	# Change the frequency along the song note
		
		pauseBetweenNotes = noteDuration * pause
		time.sleep(pauseBetweenNotes)

def mario_buzzer():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.IN)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    play(melody, tempo, 1.3, 0.800)	
    
    return
#------------------------------------Buzzer Code--------------------------------

#----------------------------------Ultra Sonic Code -----------------------------
GPIO_TRIGGER1 = 16
GPIO_ECHO1 = 20
def distance1():
    # set Trigger to HIGH
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
    GPIO.setup(GPIO_ECHO1, GPIO.IN)
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
 
    return distance

GPIO_TRIGGER = 18
GPIO_ECHO = 24
def distance():
    # set Trigger to HIGH
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
 
    return distance
 

def ultra1():
    print("Waiting For the car to arrive")
    #set GPIO direction (IN / OUT)
    GPIO_TRIGGER=18
    GRIO_ECHO=24
    while True:
            a=IR1()
            if(a==0):
                barricade_error()
            dist = distance()
            print(dist)
            if(dist<30):
                break
            time.sleep(1)
    
    return

def ultra2():
    print("Waiting For the car to Leave")
    GPIO_TRIGGER=16
    GPIO_ECHO=20
    #set GPIO direction (IN / OUT)
    while True:
            dist = distance1()
            print(dist)
            if(dist<30):
                break
            time.sleep(1)
    
    return

#---------------------------------Ultra Sonic Code --------------------------------

#----------------------------------Camera Code--------------------------------
def camera():
    print("Taking a pic!")
    os.system('fswebcam -p YUYV -d /dev/video0 -r 640x480 --no-banner /home/pi/Desktop/image.jpg > output_pic.txt')
    print("Photo Taken")
    return

#---------------------------------Camera Code--------------------------------------
#---------------------------------Publish Image Code--------------------------------
def pub_image():
    os.system('python pub_image.py')
    print("Published Image")
    return

#---------------------------------Publish Image Code--------------------------------------
#---------------------------------Publish 1 Code--------------------------------
def pub_1():
    os.system('python pub1.py')
    print("Reset Request Sent")
    return

#---------------------------------Publish 1 Code--------------------------------------

#---------------------------------subscribe 1 Code--------------------------------
def sub():
    print("Waiting for the result")
    os.system('rm output.txt > output_terminal.txt')
    os.system('python sub.py > output.txt')
    f=open("output.txt","r")
    contents=f.read()
    check="1"
    if check in contents:
        return 1
    return 0
    
#---------------------------------subscribe 1 Code--------------------------------------
def start():
    print("-------------Welcome to VQMS Raspberry---------------")
    while True:
        print("---------Process Start-----------------------")
        lcd_message1="Thank You Visit Again"
        lcd_message2="IIT Guwahati"
        lcd_message3=""
        
        display()
        
        ultra1()
        init_buzzer()
        print("Waiting for command")
        sub()
        camera()
        pub_image() 
        result=sub()
        if (result==0):
            print("Dont Open!!")
            lcd_message1="Request Not found"
            lcd_message2="---Error---"
            
            display2()
            barricade_error()
            barricade_error()
            barricade_error()
            sub()
        else:
            print("Open!!")
            lcd_message1="Accepted Request"
            lcd_message2="Gate opening"
            display4()
            openDoor()
            mario_buzzer()
            ultra2()
            closeDoor()
        print("----------Process Completed")
start()
endProgram()
            
        
