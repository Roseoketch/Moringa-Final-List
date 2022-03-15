from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
