# Writing to Firebase
# User inputs plant type
# Plant type and threshold is written to Firebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pyrebase

# Fetch the service account key JSON file contents
cred = credentials.Certificate("firebase-sdk.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://kya-planter-default-rtdb.firebaseio.com/"
})

# Place user choice into num and type vars
# @Meha this is the only part you have to change
num = 4000
type = 1

# Writes to Firebase realtime database JSON tree
ref = db.reference('/')
ref.set({
    "planters":
        {
            "planter1":
            {
                "type": type,
                "threshold": num
            }
        }
})
