"""Entry point for API"""
from .app import create_app

if __name__ == "__main__":
    APP = create_app()
    my_app.run(debug=True)


# APP = create_app()
