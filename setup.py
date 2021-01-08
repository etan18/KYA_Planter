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

num = 4000
type = 1

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
