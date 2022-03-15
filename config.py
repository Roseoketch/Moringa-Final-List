import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:justin.@localhost/grades'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '56'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)
    


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}
