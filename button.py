import RPi.GPIO as GPIO
import time
import datetime
 
button_pin = 20
led_pin = 21
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN)

global temp
temp=True

def Bstatus(ss):
	global temp
	if temp == ss:
		print ss
		temp = not temp	

while True:
	Bstatus(GPIO.input(button_pin))
	if GPIO.input(button_pin):
		GPIO.output(led_pin,True)
		time.sleep(0.1)
		GPIO.output(led_pin,False)
#		print datetime.datetime.now().microsecond
#	else:
#		print "no"
#		time.sleep(0.2)  
