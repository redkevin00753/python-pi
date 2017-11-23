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

def record(): 
	tmax = 1500
	L = [10]
	print "record your click"
	while True:
		count = 0
		for i in range(tmax):
			if GPIO.input(button_pin):
				L.append(i)
				print i
				GPIO.output(led_pin,True)
				time.sleep(0.05)
				GPIO.output(led_pin,False)
				break
			else:
				time.sleep(0.001)
				count = count + 1
#		if len(L) >= 7:
		if count >= tmax:
			break
	return L

def replay(L):
	print "replay your click ... "
	time.sleep(0.2)
	for i in L:
#		print i
		time.sleep(float(i)/1000)
		GPIO.output(led_pin,True)
		GPIO.output(m_pin,True)
		time.sleep(0.05)
		GPIO.output(led_pin,False)
		GPIO.output(m_pin,False)

def main():
	while True:
		if GPIO.input(button_pin):
			GPIO.output(led_pin,True)
			time.sleep(0.05)
			GPIO.output(led_pin,False)
			replay(record())
if __name__ == '__main__':
    main()
