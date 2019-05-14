from flask import Blueprint, current_app, jsonify, request

user_controller = Blueprint('user', __name__)

# Create
@user_controller.route('/api/users', method=['POST'])
def create_user():
    pass

# Read
@user_controller.route('/api/users/<int:user_id>', method=['GET'])
def read_user(user_id):
    pass

# Read List
@user_controller.route('/api/users', method=['GET'])
def read_user_list(user_id):
    pass

# Update
@user_controller.route('/api/users/<int:user_id>', method=['PUT'])
def update_user(user_id):
    pass

# Delete
@user_controller.route('/api/users/<int:user_id>', method=['DELETE'])
def delete_user(user_id):
    pass
