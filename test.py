import RPi.GPIO as GPIO
import time
 
led_pin = 21
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
 
print "linker led pin 24 (BCM GPIO)"
 
while True:
 
    GPIO.output(led_pin,True)
    time.sleep(0.02)
    GPIO.output(led_pin,False)
    time.sleep(1)
