#!/usr/bin/env python
# Read temperature in Celsius from sensor and translate to Fahrenheit
# Revision:
# 2017-01-29: Initial
# TODO : 


import os
import glob
import time
#initialize the device 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
	timestamp = os.system('date')
        return temp_c, timestamp 
	
while True:
	print(read_temp())	
	time.sleep(1)


### NOTES : 
# check with following commands if the device is working
# if all outputs are blank device is not working
# 
#  modprobe w1-gpio 
#  modprobe w1-therm
#  cd /sys/bus/w1/devices/
#  ll
#
# FIX : 
# 
# add following string on end of file : /boot/config.txt
# 
# # For GPIO Thermometer : 
# dtoverlay=w1-gpio

