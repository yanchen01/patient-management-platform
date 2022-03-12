import logging

from flask import Flask, redirect
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from resources import api_blueprint


"""
App Config
"""
app = Flask(__name__)
app.register_blueprint(api_blueprint)
CORS(app)


"""
Custom logger configuration
"""
# logging.basicConfig(level=logging.DEBUG, filename="app.log",
#                     format="%(asctime)s -%(levelname)s -%(message)s")
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s -%(levelname)s -%(message)s")


"""
Database Config
"""
# if in dev env
app.config['MONGODB_SETTINGS'] = {
    'db': 'patient-management',
    'host': 'mongodb://localhost/patient-management'
}
logging.info('Local Database Connected')
db = MongoEngine(app)


@app.route('/')
def index():
    return redirect('/api/swagger')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
