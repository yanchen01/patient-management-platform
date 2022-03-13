import logging

from flask import Flask, redirect
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

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
