import RPi.GPIO as GPIO
import time

valve_pin = 4

def waterPlant(threshold):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_pin, GPIO.OUT)
    GPIO.output(valve_pin, GPIO.HIGH)
    for x in range(4):
        print("watering plant...")
        time.sleep(1)
    print("closing valve...")
    GPIO.output(valve_pin, GPIO.LOW)
    time.sleep(5)
    return
