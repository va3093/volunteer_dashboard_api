
from . import users
from .models.users import User


@users.route('/v1/users', methods=['POST'])
def create_user():
    user = User(user_name='test', email='teasdfa@eaadf.com')
    return user


@users.route('/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return "a"
