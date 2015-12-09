from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    pass_hash = db.Column(db.String(80))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    total_points = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    join_date = db.Column(db.DateTime)

    def __init__(self, email, passHash, first='', last=''):
        self.email = email
        self.pass_hash = passHash
        self.first_name = first
        self.last_name = last
        self.join_date = datetime.utcnow()

    def __repr__(self):
        return '<User Email %r>' % self.email
