import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
'''
while True:
    x = random.uniform(0.1,0.5)# it creates a random number 
    y = random.uniform(0,0.1)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(4, GPIO.LOW)
    time.sleep(y)
'''
GPIO.output(4, GPIO.LOW)
