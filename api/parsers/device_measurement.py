from flask_restx import reqparse


_measurements_parser = reqparse.RequestParser()
_measurements_parser.add_argument('id',
                                  type=str,
                                  required=True,
                                  location='json',
                                  help="This field cannot be blank.")
_measurements_parser.add_argument('device_id',
                                  type=str,
                                  required=True,
                                  location='json',
                                  help="This field cannot be blank.")
_measurements_parser.add_argument('device_type',
                                  type=str,
                                  choices=('thermometer', 'scale', 'pulse',
                                           'oximeter', 'glucometer', 'blood_pressure'),
                                  required=True,
                                  location='json',
                                  help="This field cannot be blank.")
_measurements_parser.add_argument('user_id',
                                  type=str,
                                  required=True,
                                  location='json',
                                  help="This field cannot be blank.")
_measurements_parser.add_argument('reading',
                                  type=int,
                                  required=True,
                                  location='json',
                                  help="This field cannot be blank.")
_measurements_parser.add_argument('unit',
                                  type=str,
                                  choices=('celsius', 'fahrenheit', 'lbs', 'kg', 'bpm', 'percent',
                                           'mg/dl', 'mmhg'),
                                  required=True,
                                  location='json',
                                  help="This field cannot be blank.")

_measurement_parser = reqparse.RequestParser()
_measurement_parser.add_argument('id',
                                 type=str,
                                 required=True,
                                 location='args',
                                 help="This field cannot be blank.")
_measurement_parser.add_argument('device_id',
                                 type=str,
                                 required=False,
                                 location='args',
                                 help="This field cannot be blank.")
_measurement_parser.add_argument('device_type',
                                 type=str,
                                 choices=('thermometer', 'scale', 'pulse',
                                          'oximeter', 'glucometer', 'blood_pressure'),
                                 required=False,
                                 location='args',
                                 help="This field cannot be blank.")
_measurement_parser.add_argument('user_id',
                                 type=str,
                                 required=False,
                                 location='args',
                                 help="This field cannot be blank.")
_measurement_parser.add_argument('reading',
                                 type=str,
                                 required=False,
                                 location='args',
                                 help="This field cannot be blank.")
_measurement_parser.add_argument('unit',
                                 type=str,
                                 choices=('celsius', 'fahrenheit', 'lbs', 'kg', 'bpm', 'percent',
                                          'mg/dl', 'mmhg'),
                                 required=False,
                                 location='args',
                                 help="This field cannot be blank.")


_user_measurements_parser = reqparse.RequestParser()
_user_measurements_parser.add_argument('user_id',
                                 type=str,
                                 required=True,
                                 location='args',
                                 help="This field cannot be blank.")