import RPi.GPIO as GPIO
import time
import datetime
import signal  
import atexit 

atexit.register(GPIO.cleanup)

button_pin = 20
led_pin = 21
air_pin = 24
fuel_pin = 12
fire_pin = 25
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT) 
GPIO.setup(air_pin,GPIO.OUT)
GPIO.setup(fire_pin,GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN)
GPIO.setup(fuel_pin, GPIO.OUT, initial=False)  

def setair(t):
	GPIO.output(air_pin,True)
	time.sleep(t)
	GPIO.output(air_pin,False)

def setfuel(t):
	p = GPIO.PWM(fuel_pin,50) #50HZ  
	p.start(0)
	GPIO.output(air_pin,True)
	time.sleep(1)
	for i in range(0,61,5):  
		p.ChangeDutyCycle(2.5 + 10 * i / 180) 
		time.sleep(0.02)                       
		p.ChangeDutyCycle(0)                  
		time.sleep(0.02)
	time.sleep(t*0.5)
	GPIO.output(air_pin,False)
	time.sleep(t*0.5)
	for i in range(61,0,-5):  
		p.ChangeDutyCycle(2.5 + 10 * i / 180)  
		time.sleep(0.02)  
		p.ChangeDutyCycle(0)  
		time.sleep(0.02)
	time.sleep(0.5) 

def dofire():
	GPIO.output(fire_pin,True)
	time.sleep(0.5)
	GPIO.output(fire_pin,False)

def led(t):
	GPIO.output(led_pin,True)
	time.sleep(t)
	GPIO.output(led_pin,False)

def main():
	while True:
		if GPIO.input(button_pin):
			led(0.2)
			print "clean GUN Box.."
#			setair(2)
			print "fill fuel.."
			setfuel(3)
			print "fire ..."
			dofire()
			led(0.5)

if __name__ == '__main__':
    main()

