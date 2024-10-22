import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(r"hello.json") # Change the sdk path accordingly

        firebase_admin.initialize_app(cred)

    # Get a reference to the Firestore database
    db = firestore.client()
    return db