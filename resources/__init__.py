from flask import Blueprint
from flask_restx import Api

from .device import device_ns

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint, title='Patient Management API', doc='/swagger')

""" 
Namespace registering
"""
api.add_namespace(device_ns)