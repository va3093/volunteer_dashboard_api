from flask import Blueprint


users = Blueprint('users', __name__)


@users.route('/v1/users', methods=['POST'])
def create_user():
    return "a"


@users.route('/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return "a"
