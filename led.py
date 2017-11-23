import RPi.GPIO as GPIO
import time
 
led_pin = 21
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
 
dt=(303,490,200,678,100,999,1234,2222,123,444)
for i in dt:
	GPIO.output(led_pin,True)
	time.sleep(0.2)
	GPIO.output(led_pin,False)
	time.sleep(float(i)/1000)
	print str(i),float(i)/1000  
