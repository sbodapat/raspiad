#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import subprocess
import os
import glob
import time
import Image

GPIO.setmode(GPIO.BOARD)

# GPIO 17 is set up as input, pulled up to avoid false detection.
# The Port is wired to connect to GND on button press.  
# So we'll be setting up falling edge detection
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

path ='/media/usb/'

def displayThanks(channel):
	print("Event change detected.")
	#displaying the image
	image=Image.open(os.path.join(path, 'Thankyou.jpg'))
	image.show()
	time.sleep(5)
	#Take input from the numeric keypad
	raw_input("Enter your number from the keypad\n>")
	#Do the printer job over here.
	#Print job command starts over here.
	#os.startfile("print.docx","print")

while(1):
	for infile in glob.glob(os.path.join(path, '*.mp4')):
		a = subprocess.call( [ "omxplayer", "-o", "hdmi", infile])
		GPIO.add_event_detect(17, GPIO.FALLING, callback=displayThanks, bouncetime=350)