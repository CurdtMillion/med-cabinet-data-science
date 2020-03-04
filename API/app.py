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
from .models import DB, Strain

# import model
#from nearest_neighbors_model import predict


####################################################

import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

# changed from relative to to full path
model = pickle.load(open("../models/nearest_neighbors_model.sav", "rb"))
transformer = pickle.load(open("../models/transformer.sav", "rb"))
strains = pd.read_csv("../src/data/nn_model_strains.csv")


def predict(request_text):
    transformed = transformer.transform([request_text])
    dense = transformed.todense()
    recommendations = model.kneighbors(dense)[1][0]
    output_array = []
    for recommendation in recommendations:
        strain = strains.iloc[recommendation]
        output = strain.drop(['Unnamed: 0', 'name', 'ailment', 'all_text', 'lemmas']).to_dict()
        output_array.append(output)
    return output_array

##################################################


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    # consider using config
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
    @app.route("/test", methods=['POST', 'GET'])
    def predict_strain():
        text = request.get_json(force=True)
        predictions = predict(text)
        return jsonify(predictions)
    
    return app
