# standard imports
import os
import requests
import operator
import re
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# application-specific imports
from flask_login import LoginManager
# blueprint imports
from blueprints.home import home as home_blueprint
from blueprints.auth import auth as auth_blueprint

# Set up Flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"


# register blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
