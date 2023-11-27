import firebase_admin
from firebase_admin import credentials, firestore

# Change for some private credentials (research on it)
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred)
db = firestore.client()
