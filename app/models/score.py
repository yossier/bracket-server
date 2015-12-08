from app import db

class Score:
    challenge_id = db.column(db.Integer, db.ForeignKey('challenge.id'))
    user_id = db.column(db.Integer, db.ForeignKey('User.id'))
    points = db.column(db.Integer)

    def __init__(self, challenge_id, user_id, points):
        self.challenge_id = challenge_id
        self.user_id = user_id
        self.points = points
