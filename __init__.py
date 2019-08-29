from flask import Flask, render_template, url_for, redirect, request, jsonify, g, session
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__.split('.')[0])

    app.config.from_mapping(
            SECRET_KEY='dev'
            )

    app.config.from_pyfile('config.py', silent = True)

    from .models import db, Ticket
    migrate = Migrate(app, db)
    db.init_app(app)

    from .ticket_routes import ticket_routes_bp
    app.register_blueprint(ticket_routes_bp)
    from .api_routes import api_routes_bp
    app.register_blueprint(api_routes_bp)

    @app.route('/')
    def get_index():
       return redirect(url_for('tickets.index'))

    @app.errorhandler(404)
    def page_not_found(error):
        return 'Error!', 404

    return app
