"""Main application and routing logic for MEDCABINET_API"""
from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db =SQLAlchemy(app)
    db.init_app(app)


    @app.route("/", methods=['POST', 'GET'])
    def root():
        return 'Minimum viable version.'

    return app
