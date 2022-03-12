from flask_mongoengine import Document
import mongoengine as me

class Device(Document):
    """
    Document schema for a device.

    Device types can include: temp, blood_pressure, glucometer, pulse, weight, blood_saturation.
    """
    # required fields
    _id = me.StringField(required=True, primary_key=True)
    type = me.StringField(required=True)
    date_purchased = me.StringField(required=True)
    firmware_version = me.StringField(required=True)
    serial_num = me.StringField(required=True)

    # optional fields
    assigned_user = me.StringField(default="")
    prescribed_doctor = me.StringField(default="")

    def _set(self, data):
        self._id = data['id']
        self.type = data['type']
        self.date_purchased = data['date_purchased']
        self.firmware_version = data['firmware_version']
        self.serial_num = data['serial_num']

        if data['assigned_user']:
            self.assigned_user = data['assigned_user']
        if data['prescribed_doctor']:
            self.prescribed_doctor = data['prescribed_doctor']

    def _update(self, data):
        for key, val in data.items():
            if val is not None and key != 'id':
                self[key] = val

    def _delete(self):
        self.delete()

    def json(self):
        return {
            "id": self._id,
            "type": self.type,
            "date_purchased": self.date_purchased,
            "firmware_version": self.firmware_version,
            "serial_num": self.serial_num,
            "assigned_user": self.assigned_user,
            "prescribed_doctor": self.prescribed_doctor
        }
