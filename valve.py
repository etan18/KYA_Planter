import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from MCP3008 import MCP3008

VALVE_PIN = 7

def init():
    cred = credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred, {'databaseURL':'https://kya-planter-default-rtdb.firebaseio.com/'})
    lev_ref = db.reference('/planters/planter1/level')
    adc = MCP3008()

def waterLevel():
    init()
    level = adc.read(channel = 1)
    print(level)
    if level < 30:
        lev_ref.update(False)
    else:
        lev_ref.update(True)

def waterPlant(threshold):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_pin, GPIO.OUT)
    GPIO.output(valve_pin, GPIO.HIGH)
    print("*WATER THE PLANT*")
    print("*ALERT SENT*")
    GPIO.output(valve_pin, GPIO.LOW)
    time.sleep(10)
    return
    GPIO.output(VALVE_PIN, 1)
    time.sleep(5)
    GPIO.output(VALVE_PIN, 0)
