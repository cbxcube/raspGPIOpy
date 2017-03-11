#!/usr/bin/env python
# LDR manager - Light Dependdent Resistor
# Revision:
# 2017-01-29: Adding timestampt to live output
# --  log file append, not rewrite in while cycle = COMPLETED
# -- 	- if log file does not exist touch it = COMPLETED
# 	- log name variable = COMPLETED 
# TODO : 
# - add user input if append or wipe log file in case it exists
 

import os
import datetime
import time
import RPi.GPIO as GPIO

# check if log exist, create if not
#
wdir=os.getcwd()
logname="/8_ldr_dev.log"
logpath=wdir+logname

print "Starting monitoring of LDR"
if os.path.exists(logpath):
	print "Logfile exist. Appending"
	# add user input here to ask if append or clear log
else:
	print "Creating Logfile: " + logpath 
	fo = open(logpath, "wb")
	fo.write('----------------------------------------------')
	fo.write(' Log file for LDR measuring ')
	fo.close()

GPIO.setwarnings(False)

DEBUG = 1
GPIO.setmode(GPIO.BCM)
 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
 
while True:                                     
		GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		LDRReading = RCtime(3)
		#print str(GetDateTime) + RCtime(3)
		#print "Debug 1 : print GetDateTime"
		print GetDateTime
		#print "Debug 2 : print RCtime(3)"
		print RCtime(3)

		# Open logfile for appending
		#fo = open("/root/gpio/workshop-kit-python-code/8_ldr_dev.log", "wb")
		#fo = open("/root/gpio/workshop-kit-python-code/8_ldr_dev.log", "ab")
		fo = open(logpath, "ab")
		fo.write (GetDateTime)
		LDRReading = str(LDRReading)
		fo.write ("\n")
		fo.write (LDRReading)
		fo.write ("\n")
		
		# Close opend file
		fo.close()
		time.sleep(1)
