from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

app.config["SECRET_KEY"] = "very-secret-word"
db = SQLAlchemy(app)
migrate = Migrate(app, db)  
login = LoginManager(app)
login.login_view = 'login'

<<<<<<< HEAD
=======
"""if not app.debug:#this section should add error reporting by email but does not seem to be working yet
	if app.config['MAIL_SERVER']:
		auth = None
		if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
			auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
		secure = None
		if app.config['MAIL_USE_TLS']:
			secure = ()
		mail_handler = SMTPHandler(
			mailhost = (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
			fromaddr='no-reply@'+ app.config['MAIL_SERVER'],
			toaddrs=app.config['ADMINS'], subject='PFPF Error',
			credentials=auth, secure=secure)
		mail_handler.setLevel(logging.ERROR)
		app.logger.addHandler(mail_handler)"""


>>>>>>> parent of 807771a (Revert "added test Javascript")
from app import routes, models, errors

