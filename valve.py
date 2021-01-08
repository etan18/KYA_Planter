import RPi.GPIO as GPIO
import time

valve_pin = 4

def waterPlant(threshold):
    GPIO.output(valve_pin, GPIO.HIGH)
    for x in range(4):
        print("watering plant...")
        sleep(1)
    print("closing valve...")
    GPIO.output(valve_pin, GPIO.LOW)
    sleep(10)
    return
