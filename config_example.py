import os
import logging
from app.common.utils import SQLAlchemyHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sqlalchemyhandler = SQLAlchemyHandler()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    WTF_CSRF_SECRET_KEY = os.environ.get(
        'WTF_CSRF_SECRET_KEY') or 'hard to guess string'


    @classmethod
    def init_app(cls, app):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sqlalchemyhandler.setFormatter(formatter)

        loggers = [logger,
                   logging.getLogger('flask.app')]

        for l in loggers:
            l.addHandler(sqlalchemyhandler)


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    RECAPTCHA_DISABLE = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'db+sqlite:///development.db'

    @classmethod
    def init_app(cls, app):
        logger.setLevel(logging.DEBUG)
        sqlalchemyhandler.setLevel(logging.DEBUG)

        super().init_app(app)


class TestingConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    RECAPTCHA_DISABLE = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'db+sqlite:///testing.db'

    @classmethod
    def init_app(cls, app):
        print(cls.SQLALCHEMY_DATABASE_URI)
        logger.setLevel(logging.DEBUG)
        sqlalchemyhandler.setLevel(logging.DEBUG)

        super().init_app(app)


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    RECAPTCHA_DISABLE = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'db+sqlite:///production.db'

    @classmethod
    def init_app(cls, app):
        logger.setLevel(logging.WARNING)
        sqlalchemyhandler.setLevel(logging.WARNING)

        super().init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
