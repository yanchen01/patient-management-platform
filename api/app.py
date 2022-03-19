import logging
import os

from flask import Flask, redirect, request
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO
from celery import Celery

from resources import api_blueprint

from models.chat import Chat, ChatRoom


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
Audio File Upload Config
"""
app.config['AUDIO_FILE_DIR'] = "speech_to_text"

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


"""
Spech To Text API
"""
worker = Celery('speech_to_text_tasks',
                broker='amqp://admin:mypass@rabbit:5672',
                backend='mongodb://mongodb_container:27017/speech_to_text')


@app.route('/speech-to-text', methods=["POST"])
def begin_task():
    audioFile = None
    try:
        audioFile = request.files['file']
    except:
        return {'message': "No file detected"}, 400

    if audioFile.filename == "":
        return {'message': "Invalid name"}, 400

    audioFile.save("speech_to_text/"+audioFile.filename)
    r = worker.send_task('task.speech_to_text', kwargs={
        'afile': audioFile.filename})
    return {"task_id": r.id}, 200


@ app.route('/speech-to-text/status/<task_id>')
def status(task_id):
    status = worker.AsyncResult(task_id, app=worker)
    return {"status": str(status.state)}, 200


@ app.route('/speech-to-text/result/<task_id>')
def result(task_id):
    result = worker.AsyncResult(task_id).result
    print('=====received result',result)
    return {'result': str(result)}, 200


"""
Chat API
"""
socketio = SocketIO(app)


def chat_room_handler(json):
    """Create a chat room"""
    new_room = ChatRoom()
    new_room._set(json)
    try:
        new_room.save()
        socketio.emit('room_created', {
                      'status': 'success', 'room_id': new_room.get_id()})
    except:
        socketio.emit('room_created', {'status': 'failed'})


def message_handler(json):
    """Update the message to a chat room"""
    """
    Expects json: {
        chat_room_id: str,
        chat: {
            id: str,
            from_user: str,
            to_user: str,
            content: str,
            attachment: optional|str
        }
    }
    """
    # find the chat room object
    chat_room = ChatRoom.objects(_id=json['chat_room_id'])
    # make a new chat and add to the chat room
    new_chat = Chat()
    new_chat._set(json['chat'])

    try:
        new_chat.save()
        chat_room._add_chat(new_chat)

        socketio.emit('message_received', {'status': 'sent'})
    except:
        socketio.emit('message_received', {'status': 'failed'})


socketio.on('new_room', chat_room_handler)
socketio.on('new_message', message_handler)


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=4000)
    # app.run(debug=True, host="0.0.0.0", port=4000)
