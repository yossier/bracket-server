from app import db
from datetime import datetime

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer)
    title = db.Column(db.String(80), unique=True)
    pub_date = db.Column(db.DateTime)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
                               backref=db.backref('challenges', lazy='dynamic'))
    
    def __init__(self, points, title, category):
        self.points = points
        self.title = title
        self.pub_date = datetime.utcnow()
        self.category = category
        
