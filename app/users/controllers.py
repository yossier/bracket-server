from flask import Blueprint, json, request
from flask.ext.sqlalchemy import sqlalchemy
from app import db
from app.models.user import User
from app.models.challenge import Challenge
from app.models.score import Score

users = Blueprint('users', __name__)

@users.route('/users', methods=['POST'])
def users_create():
    req_json = request.get_json()

    if req_json is None:
        response = json.jsonify(error='Please post your request in json format', status=400)
        response.status_code=400
        return response
    
    email = req_json.get('email')
    passHash = req_json.get('passHash')
    first = req_json.get('first_name')
    last = req_json.get('last_name')

    if not email and not passHash:
        response = json.jsonify(error='Please Enter a valid email and password', status=400)
        response.status_code = 400
        return response
    if not email:
        response = json.jsonify(error='Please Enter a valid email address', status=400)
        response.status_code = 400
        return response
    if not passHash:
        response = json.jsonify(error='Please Enter a valid password', status=400)
        response.status_code = 400
        return response
    
    new_user = User(email, passHash, first, last)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print ("e")
        db.session.rollback()
        db.session.flush()
        response = json.jsonify(error="Email address is already registered", status=400)
        response.status_code=400
        return response
    
    response = json.jsonify(user_id=new_user.id, status=201)
    response.status_code = 201
    return response

@users.route('/users/<int:userid>', methods=['GET', 'DELETE'])
def get_delete_user_by_id(userid):
    
    user = User.query.get(userid)

    response = ''
    
    if not user:
        response = json.jsonify(error='User %i does not exist' % (userid,), status=404 )
        response.status_code=404
        return response

    if request.method == 'GET':

        scores = user.scores.all()
        completed_challenges = 0
        for score in scores:
            if score.completed:
                completed_challenges += 1
        
        response = json.jsonify(user_id=user.id, email=user.email, first_name=user.first_name, last_name=user.last_name, attempted_challenges=len(scores), completed_challenges=completed_challenges ,total_points=user.total_points, status=200)
        response.status_code=200

    if request.method == "DELETE":
        # delete target user
        response = json.jsonify(error="Unable to delete users at this time", status=400)
        response.status_code=400

    return response

@users.route('/users/authenticate', methods=['POST'])
def user_authenticate():
    req_json = request.get_json()
    email = req_json.get('email')
    passHash = req_json.get('passHash')

    if not email and not passHash:
        response = json.jsonify(error="Please enter a valid email and password", status=400)
        response.status_code = 400
        return response
    elif not email:
        response = json.jsonify(error="Please enter a valid email", status=400)
        response.status_code = 400
        return response
    elif not passHash:
        response = json.jsonify(error="Please enter a valid password", status=400)
        response.status_code = 400
        return response

    user = User.query.filter_by(email=email).first()

    if not user:
        response = json.jsonify(error="Incorrect Email and Password combonation", status=404)
        response.status_code = 404
        return response
    elif user.pass_hash != passHash:
        response = json.jsonify(error="Incorrect Email and Password combonation", status=404)
        response.status_code = 404
        return response

    response = json.jsonify(user_id=user.id, status=200)
    response.status_code = 200
    return response
        
    

@users.route('/users/<int:userid>/name', methods=['PUT'])
def update_user_name(userid):
    user = User.query.get(userid)

    req_json = requests.get_json()
    first_name = req_json.get('first_name')
    last_name = req_json.get('last_name')
    passHash = req_json.get('passHash')

    if not passHash or not user or passHash != user.pass_hash:
        response = json.jsonify(error="Authentication error: Incorrect Userid Password combo!", status=401)
        response.status_code = 401
        return response

    user.first_name = first_name
    user.last_name = last_name
    db.session.commit()

    response = json.jsonify(user_id=user.id, first_name= user.first_name, last_name=user.last_name, status=200)
    response.status_code = 200
    return response
    

@users.route('/users/<int:userid>/email', methods=['PUT'])
def replace_user_email(userid):
    user = User.query.get(userid)

    req_json = requests.get_json()
    email = req_json.get('email')
    passHash = req_json.gety('passHash')
    
    if not passHash or not user or passHash != user.pass_hash:
        response = json.jsonify(error="Authentication error: Incorrect Userid Password combo!", status=401)
        response.status_code = 401
        return response

    if not email:
        response = json.jsonify(error="Please provide a valid email address!", status=400)
        response.status_code=400
        return response
    
    user.email = email
    db.session.commit()

    response = json.jsonify(user_id=user.id, first_name= user.first_name, last_name=user.last_name, status=200)
    response.status_code = 200
    return response

@users.route('/users/<int:userid>/password', methods=['PUT'])
def replace_user_password(userid):
    user = User.query.get(userid)

    req_json = requests.get_json()
    passHash = req_json.get('passHash')
    newPassHash = req_json.get('newPassHash')
    
    if not passHash or not user or passHash != user.pass_hash:
        response = json.jsonify(error="Authentication error: Incorrect Userid Password combo!", status=401)
        response.status_code = 401
        return response

    if not newPassHash:
        response = json.jsonify(error="Please enter a valid password!", status=400)
        response.status_code = 400
        return response

    user.pash_hash = newHashPass
    db.session.commit()
    
    response = json.jsonify(user_id=user.id, status=200)
    response.status_code = 200
    return response


@users.route('/users/<int:userid>/points', methods=['GET'])
def access_user_points(userid):
    user = User.query.get(userid)
    if not user:
        response = json.jsonify(error="User %i does not exist" % (userid,), status=400)
        response.status_code=400
        return response

    response = json.jsonify(user_id=user.id, points=user.total_points, status=200)
    response.status_code=200
    return response

@users.route('/users/<int:userid>/completed-challenges', methods=['GET'])
def get_user_completed_challenges(userid):
    user = User.query.get(userid)

    if not user:
        response = json.jsonify(error="User %i does not exist" % (userid,), status=400)
        response.status_code=400
        return response
    
    scores = user.scores.all()

    challengeList = []
    num_completed_challenges = 0
    for score in scores:
        challenge = score.challenge
        if score.completed:
            num_completed_challenges += 1
        challengeList.append({"user_id":score.user_id, "user_score":score.points, "challenge_completed":score.completed, "challenge_id":challenge.id, "challenge_title":challenge.title, "challenge_category":challenge.category.name, "challenge_points":challenge.points})
    
    
    response = json.jsonify(user_id=user.id, challenges=challengeList, attempted_challenges=len(scores), completed_challenges=num_completed_challenges, status=200 )
    response.status_code=200
    return response

@users.route('/users/<int:userid>/completed-challenges/<int:challengeid>', methods=['POST', 'PUT'])
def record_user_challenge_score(userid, challengeid):
    user = User.query.get(userid)
    req_json = request.get_json()
    points =  int(req_json.get('points'))

    if not user:
        response = json.jsonify(error="User %i does not exist" % (userid,), status=400)
        response.status_code=400
        return response
    
    challenge = Challenge.query.get(challengeid)
    if not challenge:
        response = json.jsonify(error="Challenge %i does not exist" % (challengeid,), status=400)
        response.status_code=400
        return response

    if not points and points != 0:
        response = json.jsonify(error="Please provide a points value to update score by", status=400)
        response.status_code=400
        return response

    if points > challenge.points:
        response = json.jsonify(error="Challenge max score is %i" % (challenge.points), status=400)
        response.status_code = 400
        return response
    
    current_score = user.scores.filter_by(challenge_id=challengeid).first()

    prev_score = 0
    
    if not current_score:
        current_score = Score(points, user, challenge)
        
        
    elif current_score.points >= points:
        response = json.jsonify(msg="Here at <bracket> we use mastery grading", points=current_score.points, status=200)
        response.status_code = status=200
        return response

    else:
        prev_score = current_score.points
        current_score.points = points
        
    if current_score.points == challenge.points:
        current_score.completed = True

    user.total_points += current_score.points - prev_score
        
    db.session.commit()
    response = json.jsonify(msg="Successfully updated score", points=current_score.points, status=200)
    response.status_code = status=200
    return response
