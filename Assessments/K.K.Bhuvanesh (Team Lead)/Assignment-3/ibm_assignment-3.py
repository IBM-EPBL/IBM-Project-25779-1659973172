import time
import RPi.GPIO as GPIO
Red,Green,orange = 10,11,12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(orange, GPIO.OUT)
while True:
    GPIO.output(Red, GPIO.HIGH)
    time.sleep(18)
    GPIO.output(Red, GPIO.LOW)
    GPIO.output(orange, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(orange, GPIO.LOW)
    GPIO.output(Green, GPIO.HIGH)
    time.sleep(18)
    GPIO.output(Green, GPIO.LOW)
    GPIO.output(orange, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(orange, GPIO.LOW)
