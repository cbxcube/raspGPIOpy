#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)

loop_count = 0

def melody ():

	#short to long
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.3)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.4)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.5)

	#long to short
	GPIO.output(22,GPIO.LOW)
	time.sleep(.5)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.4)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.3)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.3)

	#switching
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.3)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.3)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.3)
	
os.system('clear')
print "Playing Melody... Can this be considered as a melody??!"
loop_count = input("How many times would you like melody to loop?: ")
while loop_count > 0:
	loop_count = loop_count - 1
	melody ()
