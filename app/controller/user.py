from flask import Blueprint, current_app, jsonify, request

user_controller = Blueprint('user', __name__)


@user_controller.route('/api/user', method=['POST'])
def create_user():
    pass


@user_controller.route('/api/user/<int:user_id>', method=['GET'])
def read_user(user_id):
    pass


@user_controller.route('/api/user/<int:user_id>', method=['PUT'])
def update_user(user_id):
    pass


@user_controller.route('/api/user/<int:user_id>', method=['DELETE'])
def delete_user(user_id):
    pass
