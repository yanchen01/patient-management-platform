from flask_mongoengine import Document
import mongoengine as me


class User(Document):
    _id = me.StringField(required=True, primary_key=True)
    first_name = me.StringField(max_length=40, required=True)
    last_name = me.StringField(max_length=40, required=True)
    email = me.EmailField(required=True)
    password = me.StringField(required=True)
    user_role = me.StringField(min_value=1, max_value=6, required=True)
    gender = me.StringField(max_length=40, required=True)
    date_of_birth = me.StringField(max_length=40, required=True)
    address = me.StringField(max_length=40, required=True)
    age = me.IntField(min_value=0, max_value=200, required=True)

    def _set(self, data):
        self._id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.user_role = data['user_role']
        self.gender = data['gender']
        self.date_of_birth = data['date_of_birth']
        self.address = data['address']
        self.age = data['age']

    def _update(self, data):
        for key, val in data.items():
            if val is not None and key != 'id':
                self[key] = val

    def _delete(self):
        self.delete()

    def check_password(self, password):
        return self.password == password

    def json(self):
        return {
            'id': self._id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'user_role': self.user_role,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth,
            'address': self.address,
            'age': self.age
        }
