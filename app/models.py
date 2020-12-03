from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    Measurements = db.relationship('Measurements', backref = 'user', lazy='dynamic')

    def set_password(self, password):
   	    self.password_hash=generate_password_hash(password)

    def check_password(self, password):
   	    return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}'.format(self.username)

class Measurements(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	waist = db.Column(db.Float(10))
	hips = db.Column(db.Float(10))
	bust = db.Column(db.Float(10))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Measurements {}>'.format(self.waist, self.hips, self.bust) 

@login.user_loader
def Load_User(id):
	return User.query.get(int(id))