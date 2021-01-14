#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
from valve import waterPlant
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from MCP3008 import MCP3008

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://kya-planter-default-rtdb.firebaseio.com/'})

ref = db.reference('/planters/planter1/threshold')
threshold = ref.get()
print("moisture threshold is set to " + str(threshold))

alert = False
adc = MCP3008()

while True:
    moisture = adc.read(channel = 0)
    #for MP2 demo use only - prints timestamp followed by sensor reading
    ct = datetime.datetime.now()
    print("current time:-", ct)
    print("current moisture level is " + str(moisture))

    if moisture <= threshold:
        pass
    else:
        alert = True

    if alert:
        waterPlant(threshold)
        alert = False

    time.sleep(5)
