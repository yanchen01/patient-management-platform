from flask import Blueprint
from flask_restx import Api

from .device import device_ns
from .user import user_ns
from .device_measurement import measurement_ns

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint, title='Patient Management API', doc='/swagger')

""" 
Namespace registering
"""
api.add_namespace(device_ns)
api.add_namespace(user_ns)
api.add_namespace(measurement_ns)