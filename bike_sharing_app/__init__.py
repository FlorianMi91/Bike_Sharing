from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_applicationinsights import ApplicationInsights

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

# insight pour les logs sur azure :
insight = ApplicationInsights(instrumentation_key='7269625c-4137-42ed-b32b-1d89e1835928')
insight.init_app(app)

from .routes import *
from .models import *

# models.init_db()