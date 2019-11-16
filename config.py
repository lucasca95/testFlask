

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "Culosucio"

    DB_NAME = "cicd"
    DB_USERNAME = "root"
    DB_PASSWORD = "Culosucio"

    UPLOADS = "/home/lucasca95/FlaskUploads"

    SESSION_COOKIE_CACHE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = False
    SESSION_COOKIE_CACHE = False

class TestingConfig(Config):
    TESTING=True
    SESSION_COOKIE_CACHE = False
