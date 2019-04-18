import logging
import os

from flask import Blueprint, Flask

from app.utils import common


def create_app(config_path=None):

    app = Flask(__name__)

    if config_path is None and 'PROJECT_SETTINGS' in os.environ:
        app.config.from_object(os.environ['PROJECT_SETTINGS'])
    else:
        config = common.import_config(config_path)

        for key, value in dict(config['FLASK']).items():
            app.config[key] = value

    from .controller.user import user_controller
    app.register_blueprint(user_controller)

    return app
