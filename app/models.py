from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    bust = db.Column(db.Float(10))
    waist = db.Column(db.Float(10))
    hips = db.Column(db.Float(10))
    w2k = db.Column(db.Float(10))
    k2a = db.Column(db.Float(10))
    

    def set_password(self, password):
   	    self.password_hash=generate_password_hash(password)

    def check_password(self, password):
   	    return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}'.format(self.username)

    def avatar(self, size):
    	digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    	return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
    		digest, size)


@login.user_loader
def Load_User(id):
	return User.query.get(int(id))