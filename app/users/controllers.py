from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/users', methods=['POST'])
def users_create():
    req_json = request.get_json()

    email = req_json().get('email')
    passHash = req_json.get('passHash')
    first = req_json.get('first')
    last = req_json.get('last')
    return

@users.route('/users/<userid>', methods=['GET', 'PATCH', 'DELETE'])
def get_user_by_id(userid):
    return 'You are asking for user ' + userid



@users.route('/users/<userid>/password', methods=['PUT'])
def replace_user_password(userid):
    return 'You are trying to replace ' + userid + '\'s password'


@users.route('/users/<userid>/points', methods=['GET', 'PUT'])
def access_user_points(userid):
    return

@users.route('/users/<userid>/completed-challenges', methods=['GET'])
def get_user_completed_challenges(userid):
    return

@users.route('/users/<userid>/completed-challenges/<challengeid>', methods=['POST', 'PUT'])
def record_user_challenge_score(userid, challengeid):
    return
