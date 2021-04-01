#!/usr/bin/python
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from MCP3008 import MCP3008
from sys import exit
import time

VALVE_PIN = 4

def init():
    cred = credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred, {'databaseURL':'https://kya-planter-default-rtdb.firebaseio.com/'})

def waterPlant(threshold):
    print("watering plant")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(VALVE_PIN, GPIO.OUT)
    GPIO.output(VALVE_PIN, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(VALVE_PIN, GPIO.LOW)

def waterLevel(ref):
    level = adc.read(channel = 1)
    print("current water level is " + str(level))
    ref.update({"level":level})
    if level > 13:
        ref.update({"refill":False})
        return False
    else:
        ref.update({"refill":True})
        return True

def soilMoisture(ref):
    moisture = adc.read(channel = 0)
    print("current moisture is " + str(moisture))
    ref.update({"moisture":moisture})
    return moisture

if __name__ == "__main__":
    init()
    ref = db.reference("/planters/planter1")
    # lev_ref = db.reference('/planters/planter1/level alert')
    thresh_ref = db.reference('/planters/planter1/threshold')

    threshold = thresh_ref.get()
    print("moisture threshold is set to " + str(threshold))

    alert = False
    adc = MCP3008()
    # soil_ref = db.reference('/planters/planter1/moisture')
    try:
        while True:
            threshold = thresh_ref.get()
            waterLevel(ref)
            if soilMoisture(ref) <= threshold:
                pass
            else:
                waterPlant(threshold)
            time.sleep(15)

    except KeyboardInterrupt:
        # Control-C causes KeyboardInterrupt
        pass
    GPIO.cleanup()
