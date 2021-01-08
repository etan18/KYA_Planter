#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import pyrebase
from valve import waterPlant
from firebase_admin import db

config = {
  "apiKey": "AAAAUz-gorQ:APA91bEDeqzvp3xUQvUG1C2NfJBKI4k_61mJdBscKE0w0WFpTHabbYJ2_eNAhMmr_G1h7GyXbNwfS-VvvO-_z0vml0YOArcYY80oznmeO-F8dfPBFgt3z_Fu6GcafeaEUBot9JPrp4-9",
  "authDomain": "kya-planter.firebaseapp.com",
  "databaseURL": "https://kya-planter-default-rtdb.firebaseio.com/",
  "storageBucket": "kya-planter.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

#GPIO SETUP
r1 = 4
r2 = 5
r3 = 6
r4 = 7
r5 = 8
r6 = 9
GPIO.setmode(GPIO.BCM)
GPIO.setup(r1, GPIO.IN)
GPIO.setup(r2, GPIO.IN)
GPIO.setup(r3, GPIO.IN)
GPIO.setup(r4, GPIO.IN)
GPIO.setup(r5, GPIO.IN)
GPIO.setup(r6, GPIO.IN)

valve_open = False

database = firebase.database()
threshold = database.child("planters").child("planter1").child("threshold").get().val()
print("moisture threshold is set to " + threshold)

while True:
    moisture = GPIO.input(r1) + (2*GPIO.input(r2)) + (4*GPIO.input(r3)) + (8*GPIO.input(r4))
    #for MP2 demo use only - prints timestamp followed by sensor reading
    ct = datetime.datetime.now()
    print("current time:-", ct)
    print("current moisture level is" + str(moisture / 15))

    if GPIO.input(r6):
        pass
    elif GPIO.input(r5):
        pass
    else:
        if moisture <= threshold:
            pass
        else:
            alert = True
    if alert:
        waterPlant(threshold);


    sleep(5)
