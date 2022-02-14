import os
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import requests
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://device_mongodb_container_1/devices',
    'port': 27017,
}
db = MongoEngine(app)
CORS(app)


class Device(db.Document):
    name = db.StringField(required=True)


@app.route('/devices')
def get_devices():
    devices = Device.objects()
    return jsonify(devices), 200


@app.route('/devices', methods=["POST"])
def add_devices():
    body = request.get_json()
    device = Device(**body).save()
    return jsonify(device), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
