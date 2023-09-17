# app/factory.py

from flask import Flask
from .config import Configuration
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register your blueprints or routes here, if any.

    return app
# In your app/__init__.py file, import the create_app function and create the app instance:
# python
# Copy code
# app/__init__.py

# With this structure in place, you'll be able to import create_app in your seeder.py script and create the app instance correctly. Your seeder.py script should now work without any import errors.

# Here's the updated seeder.py script:

# python
# Copy code
# seeder.py

import os
from dotenv import load_dotenv
from app.factory import create_app, db


# Load environment variables from .env
load_dotenv()

# Create a Flask app context
app = create_app()

# Rest of the seeder script remains the same...
# Make these changes, and you should be able to run the seeder.py script without any import errors.
