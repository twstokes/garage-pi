#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
# increasing to 1 second from .5 - first try after long break fails
# note - still not working on the first try after long break
# still didn't work after using wireless remote (from the vehicle) first to see if the system needed to be "energized"
# assuming it's on the RPi end at this point
# for testing purposes we may need to increase the sleep time even more to see if it will eventually work on the first try, but with a much longer delay
# do we really need to clean up and shut down the pins every time? can they stay active all the time since it is the purpose?
time.sleep(1)
GPIO.output(18, False)
GPIO.cleanup()
