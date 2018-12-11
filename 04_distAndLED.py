#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button

## Distance setup
def checkdist():
	GPIO.output(16, GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(16, GPIO.LOW)
	while not GPIO.input(18):
		pass
	t1 = time.time()
	while GPIO.input(18):
		pass
	t2 = time.time()
	return (t2-t1)*340/2


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN)
time.sleep(2)

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
        ## Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off

def loop():
	while True:
                ## Check whether the button is pressed or not.
	        ##if GPIO.input(BtnPin) == GPIO.LOW:
                if checkdist() > 0.50:
			print '...led on'
			GPIO.output(LedPin, GPIO.LOW)  # led on
		else:
			print 'led off...'
			GPIO.output(LedPin, GPIO.HIGH) # led off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
        ## When 'Ctrl+C' is pressed destroy() will be  executed.
	except KeyboardInterrupt:  
		destroy()

