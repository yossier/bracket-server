from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    passHash = db.Column(db.String(80))
    firstName = db.Column(db.String(40))
    lastName = db.Column(db.String(40))
    totalPoints = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, email, passHash, first='', last=''):
        self.email = email
        self.passHash = passHash
        self.firstName = first
        self.lastName = last

    def __repr__(self):
        return '<User Email %r>' % self.email
