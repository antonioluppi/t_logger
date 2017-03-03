#! /usr/bin/env python3
import serial
import csv
import sys
import time
#excel stuff
#from time import gmtime, strftime
#resultFile=open('MyData.csv','wb')
#end excel stuff
 

if __name__=='__main__':
	ser = serial.Serial('/dev/ttyACM0', 9600)
	f = open('output.csv', 'w+')	
	while True:
		# Read a line and convert it from b'xxx\r\n' to xxx
		line = str(time.time()) + ",\t" + ser.readline().decode('utf-8')
		print(line)
		if line:  # If it isn't a blank line
			f.write(line)
	f.close()
	ser.close()

