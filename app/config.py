class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass