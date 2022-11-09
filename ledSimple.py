#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime

# setting up GPIO
DAY = 86400  # number of seconds in a day
x = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)  # green light
GPIO.setup(26, GPIO.OUT)  # yellow light
GPIO.output(16, 0)
GPIO.output(26, 0)
test = True
binWeek = 1

try:
    while True:
        # if ("Saturday" == x.strftime("%A")):
        if (binWeek == 1):  # normal bin only
            GPIO.output(16, True)
            time.sleep(30)
            binWeek = 2

        else:  # recycle & normal bin
            GPIO.output(26, True)
            GPIO.output(16, True)
            time.sleep(30)
            binWeek = 1

        GPIO.output(26, False)
        GPIO.output(16, False)


except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    print("\nYou killed me :(")

except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
    print("Other error or exception occurred!")

finally:
    GPIO.cleanup()  # this ensures a clean exit
