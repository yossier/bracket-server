from app import db

class Challenge:
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(60))
    points = db.Column(db.Integer)

    def __init__(self, category, points):
        self.category = category
        self.points = points
