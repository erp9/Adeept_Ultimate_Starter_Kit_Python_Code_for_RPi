#!/usr/bin/env python
import RPi.GPIO as GPIO
import random
from time import sleep

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button

# List of magic eight ball sayings. Poof
ma8 = ('Outlook-not-so-good','My-sources-say-no','Signs-point-to-yes',
       'Without-a-doubt','Better-not-tell-you-now','Do-not-count-on-it',
       'Most-likely','You-may-rely-on-it','It-is-certain','Reply-hazy-Try-again',
       'My-reply-is-no','Very-doubtful','Uh-Yups')


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
			print random.sample(ma8,1)
			sleep(10)
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

