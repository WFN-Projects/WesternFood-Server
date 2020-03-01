from templates import app, api
from flask import request, Response
from scraper.main import get_scraped_data

@app.route('/', methods=['GET'])
def home():
    return 'yes'

@app.route('/api/login', methods=['GET'])
def login():
    # get_scraped_data(user_id, user_pass)
    # if not request.content_type == 'application/json':
        # return Response('failed', 'content_type must be application/json', 401)
    data = request.args
    # print(data)
    return get_scraped_data(data['user_id'], data['user_pass'])

#TODO: Add authentication
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user_data(user_id):
    return api.get_user_data(user_id)

#TODO: Add authentication
@app.route('/api/users/<user_id>', methods=['POST'])
def update_user(user_id):
    if not request.content_type == 'application/json':
        return Response('failed', 'content_type must be application/json', 401)

    data = request.get_json()
    return api.update_user(data, user_id)

#TODO: Add authentication, integrate with user sign up
@app.route('/api/add_user', methods=['POST'])
def add_user():
    if not request.content_type == 'application/json':
        return Response('failed', 'content_type must be application/json', 401)
    data = request.get_json()
    return api.add_user(data)
