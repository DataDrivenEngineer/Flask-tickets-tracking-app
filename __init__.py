from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__.split('.')[0])

    app.config.from_mapping(
            SECRET_KEY='dev'
            )

    app.config.from_pyfile('config.py', silent = True)

    from models import db

    migrate = Migrate(app, db)

    @app.route('/')
    def hello_world():
        return 'Hello, world!'

    return app
