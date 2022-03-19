from flask_restx import reqparse, inputs
from datetime import datetime


def date_type(date):
    """Parse date type"""
    try:
        datetime.strptime(date, "%m-%d-%Y")
    except ValueError:
        raise ValueError('This is not date type')
    return date


# Swagger documentation
date_type.__schema__ = {'type': 'string', 'format': 'mm-dd-yyyy'}


_users_parser = reqparse.RequestParser()
_users_parser.add_argument('id',
                           type=str,
                           required=True,
                           location='json',
                           help="This field cannot be blank.")
_users_parser.add_argument('first_name',
                           type=str,
                           required=True,
                           location='json',
                           help="This field cannot be blank.")
_users_parser.add_argument('last_name',
                           type=str,
                           required=True,
                           location='json',
                           help="This field cannot be blank.")
_users_parser.add_argument('email',
                           type=inputs.email(check=True),
                           required=True,
                           location='json',
                           help="This field cannot be blank.")
_users_parser.add_argument('password',
                           type=str,
                           required=True,
                           location='json',
                           help="This field cannot be blank.")
_users_parser.add_argument('user_role',
                           type=str,
                           required=True,
                           choices=("patient", "family", "nurse",
                                    "admin", "developer", "doctor"),
                           location='json',
                           help="This field cannot be blank."
                           )
_users_parser.add_argument('gender',
                           type=str,
                           required=True,
                           choices=("male", "female", "none_binary"),
                           location='json',
                           help="This field cannot be blank."
                           )
_users_parser.add_argument('date_of_birth',
                           type=date_type,
                           required=True,
                           location='json',
                           help="This field cannot be blank."
                           )
_users_parser.add_argument('address',
                           type=str,
                           required=True,
                           location='json',
                           help="This field cannot be blank."
                           )
_users_parser.add_argument('age',
                           type=int,
                           required=True,
                           location='json',
                           help="This field cannot be blank."
                           )

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('id',
                          type=str,
                          required=True,
                          location='args',
                          help="This field cannot be blank.")
_user_parser.add_argument('first_name',
                          type=str,
                          required=False,
                          location='args',
                          help="This field cannot be blank.")
_user_parser.add_argument('last_name',
                          type=str,
                          required=False,
                          location='args',
                          help="This field cannot be blank.")
_user_parser.add_argument('email',
                          type=inputs.email(check=True),
                          required=False,
                          location='args',
                          help="This field cannot be blank.")
_user_parser.add_argument('password',
                          type=str,
                          required=False,
                          location='args',
                          help="This field cannot be blank.")
_user_parser.add_argument('user_role',
                          type=str,
                          required=False,
                          choices=("patient", "family", "nurse",
                                   "admin", "developer", "doctor"),
                          location='args',
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('gender',
                          type=str,
                          required=False,
                          choices=("male", "female", "none_binary"),
                          location='args',
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('date_of_birth',
                          type=date_type,
                          required=False,
                          location='args',
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('address',
                          type=str,
                          required=False,
                          location='args',
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('age',
                          type=int,
                          required=False,
                          location='args',
                          help="This field cannot be blank."
                          )
