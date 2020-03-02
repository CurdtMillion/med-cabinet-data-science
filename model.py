import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

model = pickle.load(open("model.sav", "rb"))
transformer = pickle.load(open("transformer.sav", "rb"))
strains = pd.read_csv('strains.csv')


def predict(request_text):
    transformed = transformer.transform(request_text)
    dense = transformed.todense()
    best_recommendation = model.kneighbors(dense)[1][0][0]
    strain = strains.iloc[best_recommendation]
    output = strain.drop(['Unnamed: 0', 'name', 'ailment', 'all_text', 'lemmas']).to_dict()
    return output
