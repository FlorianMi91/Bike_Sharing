from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://fdfe7ca44fa24a889405ccf6ad6a6546@o1303890.ingest.sentry.io/6543419",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

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

# # insight pour les logs sur azure :
# insight = ApplicationInsights(instrumentation_key='7269625c-4137-42ed-b32b-1d89e1835928')
# insight.init_app(app)

from .routes import *
from .models import *

# models.init_db()