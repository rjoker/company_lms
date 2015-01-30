import os

from flask import Flask, render_template, request, redirect  # etc.
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

# Create and name Flask app
app = Flask("FlaskLoginApp")

# database connection
app.config['MONGODB_SETTINGS'] = {'HOST':os.environ.get('mongodb://heroku_app33076239:riq5nfat52nqtaeuen3o67egdn@ds031561.mongolab.com:31561/heroku_app33076239'),'DB': 'FlaskLogin'}
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.debug = os.environ.get('DEBUG',False)

db = MongoEngine(app) # connect MongoEngine with Flask App
app.session_interface = MongoEngineSessionInterface(db) # sessions w/ mongoengine

# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)
