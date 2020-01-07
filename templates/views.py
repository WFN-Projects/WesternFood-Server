from templates import app, api
from flask import request, Response

#TODO: Add authentication
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user_data(user_id):
    return api.get_user_data(user_id)

#TODO: Add authentication
@app.route('/api/users/<user_id>/transaction_history', methods=['POST'])
def add_user_transaction(user_id):
    if not request.content_type == 'application/json':
        return Response('failed', 'content_type must be application/json', 401)

    transaction = request.get_json()
    return api.add_user_transaction(transaction, user_id)

#TODO: Add authentication, integrate with user sign up
@app.route('/api/add_user', methods=['POST'])
def add_user():
    return api.add_user()
