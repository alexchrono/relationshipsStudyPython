from .factory import create_app
from .config import Configuration
from .models import db
from flask_migrate import Migrate
from flask import Flask

app = create_app()


# from . import selfmade_queries  # Import your routes (selfmade_queries) here

if __name__ == "__main__":
    app.run()
