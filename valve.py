import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from MCP3008 import MCP3008

def init():
    cred = credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred, {'databaseURL':'https://kya-planter-default-rtdb.firebaseio.com/'})

if __name__ == "__main__":
    cred = credentials.Certificate("firebase-sdk.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://kya-planter-default-rtdb.firebaseio.com/"
    })
    lev_ref = db.reference('/planters/planter1/level alert')
    adc = MCP3008()
    level = adc.read(channel = 1)
    print(level)
    if level < 30:
        lev_ref.update(False)
    else:
        lev_ref.update(True)
