import logging
import os

from flask import Blueprint, Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from app.commom.database import db
from app.models.schema import ma

try:
    from config import config
except ImportError:
    print('Please exec `cp config_example.py config.py` and edit config.py')
    exit()


def create_app(config_name):

    config_name = config_name or os.getenv('FLASK_CONFIG')
    app_config = config[config_name]

    app = Flask(__name__)
    app.config.from_object(app_config)

    db.init_app(app)
    ma.init_app(app)

    app.db = db
    app.app_context().push()

    app_config.init_app(app)

    from .controller.user import user_controller
    app.register_blueprint(user_controller)

    CORS(app)
    CSRFProtect(app)
    Migrate(app, db)

    return app
