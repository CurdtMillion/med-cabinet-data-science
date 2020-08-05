"""
Main application and routing logic
"""

import os
import pickle

import pandas as pd
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from .models import DB, Strain

# import model
# from nearest_neighbors_model import predict


####################################################


# changed from relative to to full path


strains = pd.read_csv("https://raw.githubusercontent.com/Build-Week-Med-Cabinet-3/Data-Science/master/API/nn_model_strains.csv")

transformer = TfidfVectorizer(stop_words="english", min_df=0.025, max_df=0.98, ngram_range=(1,3))

dtm = transformer.fit_transform(strains['lemmas'])
dtm = pd.DataFrame(dtm.todense(), columns=transformer.get_feature_names())

model = NearestNeighbors(n_neighbors=10, algorithm='kd_tree')
model.fit(dtm)



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
    
    # initialize the Flask-Cors extension 
    app = Flask(__name__)
    CORS(app)
    
    # load keys from .env files
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")

    
    # Create a new database session and return a new connection object.
    connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    cursor = connection.cursor()

    # bind the instance to specific flask app
    # initialize app for use with this database setup
    db = SQLAlchemy(app)
    db.init_app(app)

    # set routes
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
