from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config.from_object(Config)#(can't remember if this was needed)
app.config["SECRET_KEY"] = "very-secret-word"
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Flask mega tutorial

from app import routes, models