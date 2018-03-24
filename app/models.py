from app import db
from app import app
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(500))
    lastName = db.Column(db.String(500))
    email = db.Column(db.String(500))
    skills = db.Column(db.String(500))
    password = db.Column(db.String(500))
    passwordConfirmation = db.Column(db.String(500))
    posts = db.relationship('Posts',backref='user', lazy=True)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    content = db.Column(db.text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    article_id = db.relationship('Article', backref='section', lazy='dynamic')

