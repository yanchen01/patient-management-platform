from email.policy import default
from flask_mongoengine import Document
import mongoengine as me
from datetime import datetime


class Chat(Document):
    _id = me.StringField(required=True, primary_key=True)
    timestamp = me.DateTimeField(default=datetime.now)
    from_user = me.StringField(required=True)
    to_user = me.StringField(required=True)
    content = me.StringField(required=True)
    attachment = me.StringField(default="")

    def _set(self, data):
        self._id = data['id']
        self.from_user = data['fromUser']
        self.to_user = data['toUser']
        self.content = data['content']
        self.attachment = data['attachment']

        """
        optional fields
        """
        if data['attachment']:
            self.attachment = data['attachment']

    def _update(self, data):
        for key, val in data.items():
            if val is not None and key != 'id':
                self[key] = val

    def json(self):
        return {
            'id': self._id,
            'timestamp': self.timestamp.strftime("%m/%d/%Y, %H:%M:%S.%f"),
            'fromUser': self.from_user,
            'toUser': self.to_user,
            'content': self.content,
            'attachment': self.attachment,
        }


class ChatRoom(Document):
    _id = me.StringField(required=True, primary_key=True)
    users = me.ListField(me.StringFeild(), required=True)
    chats = me.ListField(me.EmbeddedDocumentField(Chat))

    def _set(self, data):
        self._id = data['id']
        self.users = data['users']

    def get_id(self):
        return self._id

    def _add_chat(self, chat):
        try:
            self.chats.append(chat)
            self.save()
        except:
            raise Exception('Chat Exception')
