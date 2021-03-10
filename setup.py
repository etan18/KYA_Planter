# Writing to Firebase
# User inputs plant type
# Plant type and threshold is written to Firebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def setup(pid, userNum, userType):
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate("firebase-sdk.json")
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://kya-planter-default-rtdb.firebaseio.com/"
    })

    # Writes to Firebase realtime database JSON tree
    ref = db.reference('/')
    ref.set({
        "planters":
            {
                "planter1":
                {
                    "planter id": pid,
                    "type": userType,
                    "threshold": userNum,
                    "refill": True
                }
            }
    })

# Fetch the service account key JSON file contents
cred = credentials.Certificate("firebase-sdk.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://kya-planter-default-rtdb.firebaseio.com/"
})

# Writes to Firebase realtime database JSON tree
ref = db.reference('/')
ref.set({
    "planters":
        {
            "planter1":
            {
                "planter id": "default",
                "type": 0,
                "threshold": 1024,
                "refill": True,
                "moisture": 0,
                "level": 0
            }
        }
})
