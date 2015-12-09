from app import db

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
                           backref=db.backref('scores', lazy='dynamic'))
    
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'))
    challenge = db.relationship('Challenge',
                                backref=db.backref('scores', lazy='dynamic'))

    def __init__(self, points, user, challenge):
        self.points = points
        self.user = user
        self.challenge = challenge

    def __repr__(self):
        return '<Score %i >' % self.points
