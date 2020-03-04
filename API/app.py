"""
Main application and routing logic
"""
# Standard imports
import os

#  Database + Heroku + Postgres
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from .models import DB

# import model
from nearest_neighbors_model import predict


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    # binding the instance to a very specific Flask app
    # initialize app for use with this database setup
    db = SQLAlchemy(app)
    db.init_app(app)

    # root route
    @app.route('/')
    def root():
        DB.create_all()
        return "Welcome to Med Cab"

    # TODO: Make text value dynamic
    @app.route("/test", methods=['GET'])
    def predict_strain(text='I have fibromyalgia and I want pain relief'):
        predictions = predict(text)
        return jsonify(predictions)
    
    return app
