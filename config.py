class Config(object):
    DEBUG = False
    TESTING = False

    # DB = ""
    # DB_USERNAME = ""
    # DB_PASSWD = ""

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = "127.0.0.1:8000"