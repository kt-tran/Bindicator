
#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime

# setting up GPIO
DAY = 86400 # number of seconds in a day
x = datetime.datetime.now()
CurrentWeek = x.isocalendar()[1] #for testing, try test_minute = datetime.datetime.now().minute
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT) #green light
GPIO.setup(26, GPIO.OUT) #yellow light
GPIO.output(16, 0)
GPIO.output(26, 0)
running = True


try:
    while running:
        if (CurrentWeek % 2 == 0): #recycle & normal bin when the week of the year is even
            GPIO.output(26, True)
            GPIO.output(16, True)
            time.sleep(DAY)

        else: #normal bin only when the week of the year is odd
            GPIO.output(16, True)
            time.sleep(DAY)

        GPIO.output(26, False)
        GPIO.output(16, False)

        running = False #exit while loop
            

  
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
    GPIO.cleanup() # this ensures a clean exit
    quit()