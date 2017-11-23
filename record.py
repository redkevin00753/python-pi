import RPi.GPIO as GPIO
import time
import datetime
 
button_pin = 20
led_pin = 21
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN)
 
tmax = 20
L = []
while True:
	i = 0
	for i in range(tmax):
		if GPIO.input(button_pin):
			GPIO.output(led_pin,True)
			time.sleep(0.1)
			GPIO.output(led_pin,False)
			L.append(i)
			break
	if len(L) > 5:
		break
print L

#	else:
#		print "no"
#		time.sleep(0.2)
