class Config(object):
    DEBUG = False
    TESTING = False

    DATA_FILE = 'data/Covid19Casos100000.csv'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
