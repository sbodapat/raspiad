#!/usr/bin/python
import sys
import subprocess
import os
import glob
path ='/media/usb/'
while(1):
 for infile in glob.glob(os.path.join(path, '*.mp4')):
  a = subprocess.call( [ "omxplayer", "-o", "hdmi", infile])