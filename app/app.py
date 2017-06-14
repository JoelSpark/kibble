# standard imports
import os
import requests
import operator
import re
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# application-specific imports

# Set up Flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
