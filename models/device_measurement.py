from flask_mongoengine import Document
import mongoengine as me
from datetime import datetime


class DeviceMeasurement(Document):
    _id = me.StringField(required=True, primary_key=True)
    device_id = me.StringField(required=True)
    device_type = me.StringField(required=True)
    user_id = me.StringField(required=True)
    reading = me.IntField(required=True)
    unit = me.StringField(required=True)
    timestamp = me.DateTimeField(default=datetime.now)

    def __validate_fields(self, data):
        """Private method to validate data fields"""
        device_type = data["device_type"]
        unit = data["unit"]
        if device_type == "thermometer":
            if unit != "celsius" and unit != "fahrenheit":
                raise ValueError
        if device_type == "scale":
            if unit != "lbs" and unit != "kg":
                raise ValueError
        if device_type == "pulse":
            if unit != "bpm":
                raise ValueError
        if device_type == "oximeter":
            if unit != "percent":
                raise ValueError
        if device_type == "glucometer":
            if unit != "mg/dl":
                raise ValueError
        if device_type == "blood_pressure":
            if unit != "mmhg":
                raise ValueError
    
    def _delete(self):
        self.delete()

    def _set(self, data):
        self.__validate_fields(data)
        self._id = data['id']
        self.device_id = data['device_id']
        self.device_type = data['device_type']
        self.user_id = data["user_id"]
        self.reading = data['reading']
        self.unit = data['unit']

    def _update(self, data):
        for key, val in data.items():
            if val is not None and key != 'id':
                self[key] = val

    def json(self):
        return {
            'id': self._id,
            'device_id': self.device_id,
            'device_type': self.device_type,
            'reading': self.reading,
            'unit': self.unit,
            'user_id': self.user_id,
            'timestamp': self.timestamp.strftime("%m/%d/%Y, %H:%M:%S.%f")
        }
