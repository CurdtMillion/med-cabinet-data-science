"""Main application and routing logic for MEDCABINET_API"""
from flask import Flask, jsonify
from decouple import config
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db =SQLAlchemy(app)
    db.init_app(app)

    test_string = """I have no appetite and want to feel euphoria.
    Also I suffer from insomnia and like fruity flavors"""

    returned_values = [{1: [{'Strain': 'Fruity-Pebbles'},
                            {'Type': 'hybrid'},
                            {'Effects': 'Happy,Relaxed,Uplifted,Euphoric,Giggly'},
                            {'Flavor': 'Sweet,Tropical,Berry'},
                            {'Description': 'Fruity Pebbles (AKA Fruity Pebbles OG) by Alien Genetics was a limited-time offering from the breeder. This sweet hybrid takes genetics from Green Ribbon, Granddaddy Purple, and Tahoe Alien\xa0to create a tropical, berry flavor reminiscent of the cereal. The euphoric effects will keep you happy when you’re stressed and help you catch some sleep when faced with insomnia. Sit back, relax, and pour yourself a bowl of Fruity Pebbles!'}]}]


    @app.route("/")
    def root():
        """Root page
        
        Returns:
            Should provide a link to base.html
        """
        return 'Minimum viable version.'
    
    @app.route("/test/", methods=['GET', 'POST'])
    def test_search(user_input=test_string):
        """Takes the input and predicts set of recommendations"""

        return jsonify(user_input, returned_values)

    return app
