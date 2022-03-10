from flask_restx import Resource, reqparse, Namespace
from models.device import Device as DeviceModel

device_ns = Namespace('device', 'Device methods')

_device_parser = reqparse.RequestParser()
_device_parser.add_argument('name',
                            type=str,
                            required=True,
                            location=['form', 'json'],
                            help="This field cannot be blank.")


@device_ns.route('/register')
class DeviceRegister(Resource):
    """
    API Resource for registering a device
    """
    @device_ns.doc(
        responses={
            200: "Register successful.",
            400: "Register unsuccessful.",
        },
        params={
            'name': {
                'in': 'formData',
                'required': True
            },
        })
    def post(self):
        data = _device_parser.parse_args()

        # # check if current user already exist
        # device = DeviceModel.objects(name=data['name'],
        #  )

        # create new device
        new_device = DeviceModel(name=data['name'],
                                 )

        try:
            new_device.save()
            return {"message": "Device created successfully."}, 200
        except:
            return {"message": "Register unsuccessful. Please try again."}, 400
