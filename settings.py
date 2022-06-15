import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)  # For using in CSRF Protection
    TITLE = "Routing"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)
    TITLE = "Routing"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.urandom(32)
    TITLE = "Routing"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.urandom(32)
    TITLE = "Routing"
