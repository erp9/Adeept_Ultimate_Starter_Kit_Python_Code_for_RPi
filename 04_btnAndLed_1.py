#!/usr/bin/env python
import RPi.GPIO as GPIO

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button

def setup():
        # Numbers GPIOs by physical location
	GPIO.setmode(GPIO.BOARD)       
        # Set LedPin's mode is output
	GPIO.setup(LedPin, GPIO.OUT)   
        # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
        # Set LedPin high(+3.3V) to make led off
	GPIO.output(LedPin, GPIO.HIGH) 

def loop():
	while True:
                # Check whether the button is pressed or not.
		if GPIO.input(BtnPin) == GPIO.LOW: 
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
        # When 'Ctrl+C' is pressed, the child prog destroy() will be executed.
	except KeyboardInterrupt:  
		destroy()

