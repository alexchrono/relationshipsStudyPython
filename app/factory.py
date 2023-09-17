# app/factory.py

from flask import Flask
from .config import Configuration
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    # Load configuration from .env file

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register your blueprints or routes here, if any.

    return app
