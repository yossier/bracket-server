from app import db

class Score:
    points = db.column(db.Integer)

    user_id = db.column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User',
                           backref=db.backref('scores', lazy='dynamic'))
    
    challenge_id = db.column(db.Integer, db.ForeignKey('challenge.id'))
    challenge = db.relationship('Challenge',
                                backref=db.backref('scores', lazy='dynamic'))

    def __init__(self, points, user, challenge):
        self.points = points
        self.user = user
        self.challenge = challenge

    def __repr__(self):
        return '<User %r Scored %r on Challenge %r>' %(self.user_id, self.points, self.challenge_id)
