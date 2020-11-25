from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	Measurements = db.relationship('Measurements', backref = 'user', lazy='dynamic')

	def __repr__(self):
		return '<User {}'.format(self.username)

class Measurements(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	waist = db.Column(db.Float)
	hips = db.Column(db.Float)
	bust = db.Column(db.Float)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Measurements {}>'.format(self.body) 