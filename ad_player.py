#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import subprocess
import os
import glob
import time
import Image

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)	#Used to run the IR LED
GPIO.setup(7,GPIO.IN) #Setting Pin 7 as input

GPIO.output(11, TRUE) #Switching the IR LED ON.
path ='/media/usb/'

def displayThanks(channel):
	print("Event change detected.")
	#displaying the image
	image=Image.open(os.path.join(path, 'Thankyou.jpg'))
	image.show()
	time.sleep(5)
	#Do the printer job over here
	count = count++ #Incrementing the counter
	count = 0 #To check how many bottles may be... 

while(1):
 for infile in glob.glob(os.path.join(path, '*.mp4')):
  a = subprocess.call( [ "omxplayer", "-o", "hdmi", infile])
  GPIO.add_event_detect(7, GPIO.RISING, callback=displayThanks, bouncetime=5)
  