from templates import app, api

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user_data(user_id):
    return api.get_user_data(user_id)