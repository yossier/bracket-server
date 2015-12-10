from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
import os

#Create an Instance of Flask
app = Flask(__name__)
#include config from config.py
app.config.from_object(os.environ['APP_SETTINGS'])

app.secret_key = 'some_secret'
#create an instance of SQLAlchemy
db = SQLAlchemy(app)
from models.user import User
from models.category import Category
from models.challenge import Challenge
from models.score import Score

from app.users.controllers import users as users
from app.challenges.controllers import challenges as challenges
app.register_blueprint(users)
app.register_blueprint(challenges)
