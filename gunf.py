import RPi.GPIO as GPIO
import time
 
led_pin = 25
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

GPIO.output(led_pin,True)
time.sleep(0.5)
GPIO.output(led_pin,False)
