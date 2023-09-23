from . import db
from flask_login import UserMixin

# UserMixin defines id attribute 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    pronouns = db.Column(db.String(100))

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    qusOne = db.Column(db.String(15), nullable=False)
    qusTwo = db.Column(db.String(15), nullable=False)
    qusThree = db.Column(db.String(15), nullable=False)
    qusFour = db.Column(db.String(15), nullable=False)
    qusFive = db.Column(db.String(15), nullable=False)
    qusSix = db.Column(db.String(15), nullable=False)
