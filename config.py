class Config(object):
    DEBUG = False
    TESTING = False

    DATA_FILE = 'data/Covid19Casos100000.csv'

    # SQLALCHEMY_DATABASE_URI = 'postgresql://db:username@localhost/dbname'
    # DB = ""
    # DB_USERNAME = ""
    # DB_PASSWD = ""


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
