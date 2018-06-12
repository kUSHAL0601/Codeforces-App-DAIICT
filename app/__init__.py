from flask import *

from flask_sqlalchemy import SQLAlchemy

from functools import wraps

from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from app.user.controllers import mod_user
app.register_blueprint(mod_user)
db.create_all()