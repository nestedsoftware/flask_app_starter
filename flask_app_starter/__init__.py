from flask import Flask

from .hello import hello_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_blueprint)
    return app
