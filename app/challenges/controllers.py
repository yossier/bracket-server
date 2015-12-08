from flask import Blueprint

users = Blueprint('challenges', __name__)

@challenges.route('/challenges', methods=['GET'])
def get_list_of_all_challenges():
    return

@challenges.route('/challenges/<challengeType>', methods=['GET'])
def get_challenge_list_of_challenge_type(challengeType):
    return

@challenges.route('/challenges/<challengeid>', methods=['GET'])
def get_challenge(challengeid):
    return
