"""Main application and routing logic for MEDCABINET_API"""
from decouple import config
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from nearest_neighbors_model import predict
import psycopg2
import os


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)    
    app.config['SQLALCHEMY_DATABASE_URI'] = config("DB_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # load file from .env file
    load_dotenv()
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    
    # establish cursor and connection
    connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    print("CONNECTION:", connection)
    cursor = connection.cursor()
    print("CURSOR:", cursor) 
    
    
    db = SQLAlchemy(app)
    db.init_app(app)


    @app.route("/")
    def root():
        """Root page
        
        Returns:
            Should provide a link to base.html
        """
        return 'Minimum viable version.'


    return app