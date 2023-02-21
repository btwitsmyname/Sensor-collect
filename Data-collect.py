#!/usr/bin/env python3
#import libaries
import os
import sys
import time
import schedule
from sense_hat import SenseHat
import shutil
#setup libaries
sense = SenseHat()
#tempature sensor
temp = sense.get_temperature()
#humidity sensor
humidity = sense.get_humidity()
#time stamp
localtime = time.asctime(time.localtime(time.time()))
def job():
	#file naming process
	for count , f in enumerate (os.listdir()):
		a = "file("
		b = str(count)
		c = ").txt"
		d = a + b + c
		#make , open , and write to the file
		sys.stdout = open (d,"w")
		#print the time and date
		print (" the humidity is ",humidity ,"° \n the tempature is " , temp , "° \n on" , localtime)
'''
NOTE:
this wont update the sensor as it outputs the data
when the program runs it outputs the data gathered when it first runs

'''
#timer
schedule.every(10).seconds.do(job)
while True:
	schedule.run_pending()
	time.sleep(1)
