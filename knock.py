import RPi.GPIO as GPIO
import time
import datetime
 
button_pin = 20
led_pin = 21
m_pin = 24
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT) 
GPIO.setup(m_pin,GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN)
 
tmax = 2300
L = []
print "record your click"
while True:
	count = 0
	for i in range(tmax):
		if GPIO.input(button_pin):
			L.append(i)
			print i
			GPIO.output(led_pin,True)
			time.sleep(0.2)
			GPIO.output(led_pin,False)
			break
		else:
			time.sleep(0.001)
			count = count + 1
#	if len(L) >= 7:
	if count >= tmax:
		break
print "replay your click ... "
time.sleep(1)
for i in L:
	print i
	time.sleep(float(i)/1000)
	GPIO.output(led_pin,True)
	GPIO.output(m_pin,True)
	time.sleep(0.2)
	GPIO.output(led_pin,False)
	GPIO.output(m_pin,False)
