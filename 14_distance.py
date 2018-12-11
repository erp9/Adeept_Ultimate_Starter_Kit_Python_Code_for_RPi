#! /usr/bin/python
import RPi.GPIO as GPIO
import time

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
try:
	while True:
                ##print 'Distance: %0.2f m' %checkdist()
                # print '%0.2f' %checkdist() * 3               
                ##print checkdist()*3
                if checkdist() < 0.50:
                        print 'You are smelly, go away'
                else:
                        print 'Hey good looking, come over here'

                time.sleep(.1)
except KeyboardInterrupt:
	GPIO.cleanup()


