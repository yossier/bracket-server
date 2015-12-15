from app import app, db
from app.models.user import User
from app.models.challenge import Challenge
from app.models.score import Score
from app.models.category import Category
import os
app.config.from_object(os.environ["APP_SETTINGS"])

recursion = Category("recursion")
db.session.add(recursion)

dataStructures = Category("dataStructures")
db.session.add(dataStructures)

complexity =  Category("complexity")
db.session.add(complexity)

loops = Category("loops")
db.session.add(loops)

algorithms = Category("algorithms")
db.session.add(algorithms)

db.session.commit()

challenge1 = Challenge(1, "complexity1", Category.query.get(3))
db.session.add(challenge1)

challenge2 = Challenge(1, "complexity2", Category.query.get(3))
db.session.add(challenge2)

challenge3 = Challenge(1, "complexity3", Category.query.get(3))
db.session.add(challenge1)

challenge4 = Challenge(6, "loops1", Category.query.get(4))
db.session.add(challenge4)

challenge5 = Challenge(7, "loops2", Category.query.get(4))
db.session.add(challenge5)

challenge6 = Challenge(6, "loops3", Category.query.get(4))
db.session.add(challenge6)

challenge7 = Challenge(8, "loops4", Category.query.get(4))
db.session.add(challenge7)

challenge8 = Challenge(4, "recursion1", Category.query.get(1))
db.session.add(challenge8)

challenge9 = Challenge(3, "recursion2", Category.query.get(1))
db.session.add(challenge9)

challenge10 = Challenge(6, "recursion3", Category.query.get(1))
db.session.add(challenge10)

challenge11 = Challenge(6, "recursion4", Category.query.get(1))
db.session.add(challenge11)

challenge12 = Challenge(7, "dataStructures1", Category.query.get(2))
db.session.add(challenge12)

challenge13 = Challenge(8, "dataStructures2", Category.query.get(2))
db.session.add(challenge13)

challenge14 = Challenge(1, "complexity4", Category.query.get(3))
db.session.add(challenge14)

challenge15 = Challenge(9, "dataStructures3", Category.query.get(2))
db.session.add(challenge15)

challenge16 = Challenge(5, "dataStructures4", Category.query.get(2))
db.session.add(challenge16)

challenge17 = Challenge(6, "algorithms1", Category.query.get(5))
db.session.add(challenge17)

challenge18 = Challenge(6, "algorithms2", Category.query.get(5))
db.session.add(challenge18)

challenge19 = Challenge(7, "algorithms3", Category.query.get(5))
db.session.add(challenge19)

challenge20 = Challenge(5, "algorithms4", Category.query.get(5))
db.session.add(challenge20)

db.session.commit()
