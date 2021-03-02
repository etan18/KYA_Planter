#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import valve
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from MCP3008 import MCP3008

VALVE_PIN = 7

def waterPlant(threshold):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(VALVE_PIN, GPIO.OUT)
    GPIO.output(VALVE_PIN, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(VALVE_PIN, GPIO.LOW)
    return

if __name__ == "__main__":
    cred = credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred, {'databaseURL':'https://kya-planter-default-rtdb.firebaseio.com/'})

    thresh_ref = db.reference('/planters/planter1/threshold')
    threshold = thresh_ref.get()
    print("moisture threshold is set to " + str(threshold))

    alert = False
    adc = MCP3008()
    soil_ref = db.reference('/planters/planter1/moisture')

    while True:
        moisture = adc.read(channel = 0)
        soil_ref.update(moisture)

        if moisture <= threshold:
            pass
        else:
            alert = True

        if alert:
            waterPlant(threshold)
            alert = False

        time.sleep(5)
