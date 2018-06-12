from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    codeforces_id=db.Column(db.String,unique=True)
    email=db.Column(db.String,unique=True)

    def __init__(self, username, password,codeforces_id,email):
        self.username = username
        self.password = generate_password_hash(password)
        self.codeforces_id = codeforces_id
        self.email = email
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            'id' : self.id,
            'username': self.username,
            'password': self.password,
            'codeforces_id': self.codeforces_id,
            'email': self.email,
        }

    def __repr__(self):
        return "User<%d> %s" % (self.id, self.name)
