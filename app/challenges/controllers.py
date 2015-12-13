from flask import Blueprint, json, request
from flask.ext.sqlalchemy import sqlalchemy
from app import db
from app.models.user import User
from app.models.challenge import Challenge
from app.models.category import Category
from app.models.score import Score

def createSerializableList(challenges):
    challengeList = []
    for challenge in challenges:
        challengeList.append({"id":challenge.id, "points":challenge.points, "title":challenge.title, "category":challenge.category.name})
    return challengeList


challenges = Blueprint('challenges', __name__)


@challenges.route('/challenges', methods=['GET'])
def get_list_of_all_challenges():
    challenges = Challenge.query.all()
    
    response = json.jsonify(challenges=createSerializableList(challenges), status=200)
    response.status_code = 200
    return response

@challenges.route('/challenges/<string:challengeType>', methods=['GET'])
def get_challenge_list_of_challenge_type(challengeType):

    category = Category.query.filter_by(name=challengeType).first()
    challenges = category.challenges.all()

    response = json.jsonify(challenges=createSerializableList(challenges), status=200)
    response.status_code = 200
    return response

@challenges.route('/challenges/<int:challengeid>', methods=['GET'])
def get_challenge(challengeid):
    challenge = Challenge.query.get(challengeid)

    response = json.jsonify(id=challenge.id, points=challenge.points, title=challenge.title, category=challenge.category.name, status=200)
    response.status_code = 200
    return response
