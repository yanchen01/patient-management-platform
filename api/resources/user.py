from flask_restx import Resource, Namespace

# Import models
from models.user import User as UserModel

# Import parsers
from parsers.user import _users_parser, _user_parser, _user_login_parser

user_ns = Namespace('user', 'User methods')


@user_ns.route('/')
class Users(Resource):
    """
    Shows a list of users, and lets you POST to add new user
    """
    @user_ns.doc(
        responses={
            200: "User added successfully.",
            400: "Adding device unsuccessful. Please try again.",
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
            return {"message": "Adding device unsuccessful. Please try again."}, 400

    @user_ns.doc(
        response={
            200: "Get all users successful.",
            400: "Get all devices unsuccessful.",
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
