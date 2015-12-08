from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy

#Create an Instance of Flask
app = Flask(__name__)
#include config from config.py
app.config.from_object('config')

app.secret_key = 'some_secret'
#create an instance of SQLAlchemy
db = SQLAlchemy(app)
from app import models

from app.users.controllers import users as users
app.register_blueprint(users)
