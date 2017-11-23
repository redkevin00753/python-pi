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

def myLift(a=1,b=1): 
	for i in range(b):
		print i
		GPIO.output(led_pin,True)
		GPIO.output(m_pin,True)
		time.sleep(a)
		GPIO.output(led_pin,False)
		GPIO.output(m_pin,False)
		print "OK"
		time.sleep(a)
	return "All ok"


def main():
	while True:
		l=raw_input("how long to change(in second).")
		t=raw_input("how many times loop ?")
		print myLift(float(l),int(t))

if __name__ == '__main__':
    main()
