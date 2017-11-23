#!/usr/bin/env python    
  
  
import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  
  
atexit.register(GPIO.cleanup)    
  
servopin = 12  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(servopin, GPIO.OUT, initial=False)  
p = GPIO.PWM(servopin,50) #50HZ  
p.start(0)  
time.sleep(1)
o=2  
while(o > 0):  
  for i in range(61,0,5):  
    p.ChangeDutyCycle(2.5 + 10 * i / 180) 
    time.sleep(0.02)                       
    p.ChangeDutyCycle(0)                  
    time.sleep(0.02)
  time.sleep(1) 
  for i in range(0,61,5):  
    p.ChangeDutyCycle(2.5 + 10 * i / 180)  
    time.sleep(0.02)  
    p.ChangeDutyCycle(0)  
    time.sleep(0.02) 
  time.sleep(1) 
  o=o-1
  print o
