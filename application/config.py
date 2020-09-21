
import os
import logging

class BaseConfig(object):
    DEBUG = False
    TESTING = False

    # FIXME: Designate your own key
    SECRET_KEY = 'REMEMBER TO UPDATE YOUR ENCRYPTION KEY'

    # FIXME: Designate your own salt
    SECURITY_PASSWORD_SALT = 'REMEMBER TO UPDATE YOUR ENCRYPTION SALT'

    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'application.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_CONFIRMABLE = False
    CACHE_TYPE = 'simple'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


config = {
    "development": "application.config.DevelopmentConfig",
    "testing": "application.config.TestingConfig",
    "default": "application.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)