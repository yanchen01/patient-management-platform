import mongoengine as me


class Device(me.Document):
    name = me.StringField(required=True)

    # def __init__(self, name=None):
    #     self.name = name

    def json(self):
        return {
            'name': self.name,
        }
