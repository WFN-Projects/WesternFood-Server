import firebase_admin, time, google
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import ArrayUnion, SERVER_TIMESTAMP, Increment
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

#TODO: Add authentication
def update_user(data, user_id):
    try:
        user_ref = db.collection('users').document(user_id)
    except google.cloud.exceptions.NotFound:
        return Response('failed', 'User does not exist!', 401)

    if 'transaction' in data:
        transaction = data['transaction']
        user_ref.update({
            'balance': Increment(-transaction['price']),
            'transaction_history': ArrayUnion([transaction])
        })
    if 'load' in data:
        load = data['load']
        user_ref.update({
            'gross_loaded': Increment(load)
        })

    return Response('User data successfully updated', 200)

#TODO: Add authentication
def add_user(data):
    user = {
        'balance': 0,
        'gross_loaded': 0,
        'transaction_history': [],
        'joined_at': SERVER_TIMESTAMP
    }
    db.collection('users').document(data['user_id']).set(user)

    return Response('Successfully added user', 200)
