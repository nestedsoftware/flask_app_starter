import json

from flask import Blueprint

hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route('/')
def hello():
    return (json.dumps({ 'message': "Hello friend!" }), 
    	200, { 'content_type': 'application/json'})

