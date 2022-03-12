from flask_restx import reqparse
from datetime import datetime


def date_type(date):
    """Parse date type"""
    try:
        datetime.strptime(date, "%m-%d-%Y")
    except ValueError:
        raise ValueError('This is not date type')
    return date


# custom schema
date_type.__schema__ = {'type': 'string', 'format': 'mm-dd-yyyy'}


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
                             type=date_type,
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
                            type=date_type,
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
