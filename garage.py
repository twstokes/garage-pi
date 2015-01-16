#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# set the GPIO mode
GPIO.setmode(GPIO.BCM)
# set pin 18 for output
GPIO.setup(18, GPIO.OUT)
# output to pin 18
GPIO.output(18, True)
# sleep for one second
time.sleep(1)
# turn off output for pin 18
GPIO.output(18, False)
# gpio cleanup
GPIO.cleanup()
