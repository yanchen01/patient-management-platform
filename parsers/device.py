from datetime import datetime
from enum import unique
from flask_restx import reqparse

_devices_parser = reqparse.RequestParser()
_devices_parser.add_argument('id',
                             type=str,
                             required=True,
                             location=('json'),
                             help="This field cannot be blank.")
_devices_parser.add_argument('type',
                             type=str,
                             choices=('temp', 'blood_pressure', 'glucometer',
                                      'pulse', 'weight', 'blood_saturation'),
                             required=True,
                             location=('json'),
                             help="This field cannot be blank.")
_devices_parser.add_argument('date_purchased',
                             type=str,
                             required=True,
                             location=('json'),
                             help="This field cannot be blank.")
_devices_parser.add_argument('firmware_version',
                             type=str,
                             required=True,
                             location=('json'),
                             help="This field cannot be blank.")
_devices_parser.add_argument('serial_num',
                             type=str,
                             required=True,
                             location=('json'),
                             help="This field cannot be blank.")
_devices_parser.add_argument('assigned_user',
                             type=str,
                             required=False,
                             location=('json'),
                             )
_devices_parser.add_argument('prescribed_doctor',
                             type=str,
                             required=False,
                             location=('json'),
                             )


_device_parser = reqparse.RequestParser()
_device_parser.add_argument('id',
                            type=str,
                            required=True,
                            location='args',
                            help="This field cannot be blank.")
_device_parser.add_argument('type',
                             type=str,
                             choices=('temp', 'blood_pressure', 'glucometer',
                                      'pulse', 'weight', 'blood_saturation'),
                             required=False,
                             location='args',
                             help="This field cannot be blank.")
_device_parser.add_argument('date_purchased',
                             type=str,
                             required=False,
                             location='args',
                             help="This field cannot be blank.")
_device_parser.add_argument('firmware_version',
                             type=str,
                             required=False,
                             location='args',
                             help="This field cannot be blank.")
_device_parser.add_argument('serial_num',
                             type=str,
                             required=False,
                             location='args',
                             help="This field cannot be blank.")
_device_parser.add_argument('assigned_user',
                             type=str,
                             required=False,
                             location='args',
                             )
_device_parser.add_argument('prescribed_doctor',
                             type=str,
                             required=False,
                             location='args',
                             )
