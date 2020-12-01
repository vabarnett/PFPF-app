from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

app.config["SECRET_KEY"] = "very-secret-word"
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Flask mega tutorial
login = LoginManager(app)

from app import routes, models

