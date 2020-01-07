import firebase_admin, time, google
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import ArrayUnion, SERVER_TIMESTAMP
from flask import Response

cred = credentials.Certificate("westernfood-40032-firebase-adminsdk-pksgj-64f15a1877.json")
firebase_admin.initialize_app(cred, {'projectId': 'westernfood-40032'})

db = firestore.client()

#TODO: Add authentication
def get_user_data(user_id):
    user_ref = db.collection('users').document(user_id)
    try:
        user = user_ref.get()
        return user.to_dict()
    except google.cloud.exceptions.NotFound:
        return Response('failed', 'User does not exist!', 401)

#TODO: Add authentication and error if user does not exist
def add_user_transaction(transaction, user_id):
    user_ref = db.collection('users').document(user_id)
    user_ref.update({'transaction_history': ArrayUnion([transaction])})
    return Response('Transaction successfully added', 200)

#TODO: Add authentication
def add_user():
    user = {
        'balance': 0,
        'gross_loaded': 0,
        'transaction_history': [],
        'joined_at': SERVER_TIMESTAMP
    }
    db.collection('users').add(user)

    return Response('Successfully added user', 200)
