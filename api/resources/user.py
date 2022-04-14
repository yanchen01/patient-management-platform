from flask_restx import Resource, Namespace
import logging
# Import models
from models.user import User as UserModel

# Import parsers
from parsers.user import _users_parser, _user_parser, _user_login_parser, _user_add_doctor_parser, _user_add_nurse_parser, _user_add_patient_parser, _user_get_parser

user_ns = Namespace('user', 'User methods')


@user_ns.route('/')
class Users(Resource):
    """
    Shows a list of users, and lets you POST to add new user
    """
    @user_ns.doc(
        responses={
            200: "User added successfully.",
            400: "Adding User unsuccessful. Please try again.",
        },
        parser=_users_parser
    )
    def post(self):
        """Add new user"""
        data = _users_parser.parse_args()

        # create new user
        new_user = UserModel()
        new_user._set(data)

        try:
            new_user.save()
            return {"message": "User added successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Adding User unsuccessful. Please try again."}, 400

    @user_ns.doc(
        response={
            200: "Get all users successful.",
            400: "Get all users unsuccessful.",
        }
    )
    def get(self):
        """Get all users"""
        try:
            data = UserModel.objects.all()
            # serialize
            users = [user.json() for user in data]
            return {"message": "Get all users successful.", "data": users}, 200
        except:
            return {"message": "Get all users unsuccessful. Please try again."}, 400


@user_ns.route('/detail')
class User(Resource):
    """
    Shows detail about a user, and lets you DELETE, PUT a user
    """
    @user_ns.doc(
        parser=_user_parser,
        responses={
            200: "Get user successfully.",
            400: "Get user unsuccessful.",
        }
    )
    def get(self):
        """Get detail about a user"""
        data = _user_parser.parse_args()
        try:
            user = UserModel.objects(_id=data['id']).first()
            return {"message": "Get user successful", "data": user.json()}, 200
        except:
            return {"message": "Get user unsuccessful. Please try again."}, 400

    @user_ns.doc(
        parser=_user_parser,
        responses={
            200: "Update user successful.",
            400: "Update user unsuccessful.",
        }
    )
    def put(self):
        """Updates a user"""
        data = _user_parser.parse_args()
        try:
            user = UserModel.objects(_id=data['id']).first()
            user._update(data)
            user.save()
            return {"message": "Update user successful.", "data": user.json()}, 200
        except:
            return {"message": "Update user unsuccessful."}, 400

    @user_ns.doc(
        parser=_user_parser,
        responses={
            200: "Deleted user successful.",
            400: "Deleted user unsuccessful.",
        }
    )
    def delete(self):
        """Deletes a user"""
        data = _user_parser.parse_args()
        try:
            user = UserModel.objects(_id=data['id']).first()
            user._delete()
            return {"message": "Delete user successful."}, 200
        except:
            return {"message": "Delete user unsuccessful."}, 400


@user_ns.route('/login')
class Users(Resource):
    """
    Login a user
    """
    @user_ns.doc(
        responses={
            200: "User login successfully.",
            400: "User login unsuccessful. Please try again.",
        },
        parser=_user_login_parser
    )
    def post(self):
        """Log in user"""

        data = _user_login_parser.parse_args()

        # create new user
        user = UserModel.objects(_id=data['id']).first()

        if user.check_password(data['password']):
            return {"message": "User login successfully.", "data": user.json()}, 200

        return {"message": "User login unsuccessful. Please try again."}, 400

@user_ns.route('/doctor')
class Doctor(Resource):
    @user_ns.doc(
        responses={
            200: "Get doctors successfully.",
            400: "Get doctors unsuccessful. Please try again.",
        },
        parser=_user_get_parser
    )
    def get(self):
        """get a user's doctors"""
        data = _user_get_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            doctors = user.json()['doctors']
            data = []
            for doctor in doctors:
                p = UserModel.objects(_id=doctor).first()
                data.append(p.json())
            return {"message": "Get doctors successfully.", 'data': data}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Get doctors unsuccessful. Please try again."}, 400

    @user_ns.doc(
        responses={
            200: "User added doctor successfully.",
            400: "Adding doctor unsuccessful. Please try again.",
        },
        parser=_user_add_doctor_parser
    )
    def post(self):
        """Add new doctor to user"""
        data = _user_add_doctor_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            user._add_doctor(data['doctor_id'])
            user.save()

            doctor = UserModel.objects(_id=data['doctor_id']).get()
            doctor._add_patient(data['user_id'])
            doctor.save()
            return {"message": "User added doctor successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Adding doctor unsuccessful. Please try again."}, 400

    @user_ns.doc(
        responses={
            200: "Delete doctor successfully.",
            400: "Delete doctor unsuccessful. Please try again.",
        },
        parser=_user_add_doctor_parser
    )
    def delete(self):
        """Delete doctor to user"""
        data = _user_add_doctor_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            user._remove_doctor(data['doctor_id'])
            user.save()

            doctor = UserModel.objects(_id=data['doctor_id']).get()
            doctor._remove_patient(data['user_id'])
            doctor.save()
            return {"message": "Delete doctor successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Delete doctor unsuccessful. Please try again."}, 400

@user_ns.route('/nurse')
class Nurse(Resource):
    @user_ns.doc(
        responses={
            200: "Get nurses successfully.",
            400: "Get nurses unsuccessful. Please try again.",
        },
        parser=_user_get_parser
    )
    def get(self):
        """get a user's nurses"""
        data = _user_get_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            nurses = user.json()['nurses']
            data = []
            for nurse in nurses:
                p = UserModel.objects(_id=nurse).first()
                data.append(p.json())
            return {"message": "Get nurses successfully.", 'data': data}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Get nurses unsuccessful. Please try again."}, 400

    @user_ns.doc(
        responses={
            200: "User added nurse successfully.",
            400: "Adding nurse unsuccessful. Please try again.",
        },
        parser=_user_add_nurse_parser
    )
    def post(self):
        """Add new nurse to user"""
        data = _user_add_nurse_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            user._add_nurse(data['nurse_id'])
            user.save()

            nurse = UserModel.objects(_id=data['nurse_id']).get()
            nurse._add_patient(data['user_id'])
            nurse.save()
            return {"message": "User added nurse successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Adding nurse unsuccessful. Please try again."}, 400

    @user_ns.doc(
        responses={
            200: "Delete nurse successfully.",
            400: "Delete nurse unsuccessful. Please try again.",
        },
        parser=_user_add_nurse_parser
    )
    def delete(self):
        """Delete nurse to user"""
        data = _user_add_nurse_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            user._remove_nurse(data['nurse_id'])
            user.save()

            nurse = UserModel.objects(_id=data['nurse_id']).get()
            nurse._remove_patient(data['user_id'])
            nurse.save()
            return {"message": "Delete nurse successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Delete nurse unsuccessful. Please try again."}, 400

@user_ns.route('/patient')
class Patient(Resource):
    @user_ns.doc(
        responses={
            200: "Get patients successfully.",
            400: "Get patients unsuccessful. Please try again.",
        },
        parser=_user_get_parser
    )
    def get(self):
        """get a user's patients"""
        data = _user_get_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            patients = user.json()['patients']
            data = []
            for patient in patients:
                p = UserModel.objects(_id=patient).first()
                data.append(p.json())
            return {"message": "Get patients successfully.", 'data': data}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Get patients unsuccessful. Please try again."}, 400

    @user_ns.doc(
        responses={
            200: "User added patient successfully.",
            400: "Adding patient unsuccessful. Please try again.",
        },
        parser=_user_add_patient_parser
    )
    def post(self):
        """Add new patient to user"""
        data = _user_add_patient_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            user._add_patient(data['patient_id'])
            user.save()

            return {"message": "User added patient successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Adding patient unsuccessful. Please try again."}, 400

    @user_ns.doc(
        responses={
            200: "Delete patient successfully.",
            400: "Delete patient unsuccessful. Please try again.",
        },
        parser=_user_add_patient_parser
    )
    def delete(self):
        """Delete patient to user"""
        data = _user_add_patient_parser.parse_args()

        try:
            user = UserModel.objects(_id=data['user_id']).get()
            user._remove_patient(data['patient_id'])
            user.save()
            return {"message": "Delete patient successfully."}, 200
        except Exception as e:
            logging.info(e)
            return {"message": "Delete patient unsuccessful. Please try again."}, 400