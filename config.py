import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	#SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  - I have not been able to make this work

	
	SQLALCHEMY_DATABASE_URI = os.environment.get('DATABASE_URL') or \
	    'sqlite:///'+os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False