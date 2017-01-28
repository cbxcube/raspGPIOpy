#!/usr/bin/python
# PIR manager - Passive Infrared Resistor/Sensor?!
# Revision:
# 2017-01-29: Adding timestamp to output - import "os"
# 


import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

GPIO_PIR = 7

print "PIR Module Test (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0

try:
  print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    
  print "  Ready"     
  # Loop until users quits with CTRL-C
  while True :
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  ! ! ! WARNING ! ! ! Motion detected!"
      os.system('date')
      # Record previous state
      GPIO.output(27,GPIO.HIGH)
      time.sleep(1)
      GPIO.output(27,GPIO.LOW)
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  GPIO Ready! Monitoring..."
      Previous_State=0
    # Wait for 10 milliseconds
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
