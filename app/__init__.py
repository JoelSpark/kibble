# standard imports
import os
import requests
import operator
import re
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# application-specific imports
from flask_login import LoginManager

db = SQLAlchemy()


# Set up Flask app
def build_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    @app.route('/')
    def index():
        return 'Hello World'

    return app
