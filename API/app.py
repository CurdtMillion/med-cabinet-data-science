"""Main application and routing logic for MEDCABINET_API"""
from decouple import config
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from nearest_neighbors_model import predict
import psycopg2
import os

#######################################################################################################################
# """ This section to be cleaned up eventually but put in place to have a working pipeline for now"""
# import pickle
# import pandas as pd
# from sklearn.neighbors import NearestNeighbors
# from sklearn.feature_extraction.text import TfidfVectorizer

# model = pickle.load(open("../models/nearest_neighbors_model.sav", "rb"))
# transformer = pickle.load(open("../models/transformer.sav", "rb"))
# strains = pd.read_csv("../src/data/nn_model_strains.csv")


# def predict(request_text):
#     transformed = transformer.transform(request_text)
#     dense = transformed.todense()
#     best_recommendation = model.kneighbors(dense)[1][0][0]
#     strain = strains.iloc[best_recommendation]
#     output = strain.drop(['Unnamed: 0', 'name', 'ailment', 'all_text', 'lemmas']).to_dict()
#     return output
#######################################################################################################################

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

    # @app.route('/predict', methods=['POST', 'GET'])
    # def root():
    #     req_data = request.get_json(force=True)
    #     return predict(req_data)


    return app