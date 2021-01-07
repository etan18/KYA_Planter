import RPi.GPIO as GPIO
import time

valve_pin = 4

def waterPlant(threshold):
    GPIO.output(valve_pin, GPIO.HIGH)
    sleep(5)
    GPIO.output(valve_pin, GPIO.LOW)
    return
