#! /usr/bin/env python3
import serial
import csv
import sys
import time
#excel stuff
#from time import gmtime, strftime
#resultFile=open('MyData.csv','wb')
#end excel stuff
 
def scan():
    """scan for available ports. return a list of tuples (num, name)"""
    available = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            available.append( (i, s.portstr))
            s.close()   # explicit close 'cause of delayed GC in java
        except serial.SerialException:
            pass
    return available

if __name__=='__main__':
    print ("Found ports:")
    for n,s in scan():
        print ("(%d) %s" % (n,s))
    selection = input("Enter port number:")
    try:
        ser = serial.Serial(eval(selection), 9600, timeout=1)
        print("connected to: " + ser.portstr)
    except serial.SerialException:
        pass
	f = open('output.csv', 'w+')	
    while True:
        # Read a line and convert it from b'xxx\r\n' to xxx
        line = str(time.time()) + "," + ser.readline().decode('utf-8')]
        if line:  # If it isn't a blank line
            f.write(line)
    f.close()
	ser.close()

