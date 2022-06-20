from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
# app.config["SECRET_KEY"] = "very secret"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///..//user.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["WTF_CSRF_SECRET_KEY"] = os.getenv("WTF_CSRF_SECRET_KEY")

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from .routes import *
from .models import *

# models.init_db()