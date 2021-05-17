import RPi.GPIO as GPIO
import time

blue1 = 17
blue2 = 27
yellow1 = 16
yellow2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(blue1,GPIO.OUT)
GPIO.setup(blue2,GPIO.OUT)
GPIO.setup(yellow1,GPIO.OUT)
GPIO.setup(yellow2,GPIO.OUT)
print("LED on")
GPIO.output(blue1,GPIO.HIGH)
GPIO.output(blue2,GPIO.HIGH)
GPIO.output(yellow1,GPIO.HIGH)
GPIO.output(yellow2,GPIO.HIGH)
time.sleep(2)
print("LED off")
GPIO.output(blue1,GPIO.LOW)
GPIO.output(blue2,GPIO.LOW)
GPIO.output(yellow1,GPIO.LOW)
GPIO.output(yellow2,GPIO.LOW)