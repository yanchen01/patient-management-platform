from flask import jsonify
from flask_restx import Resource, Namespace
from models import device

# Import models
from models.device import Device as DeviceModel

# Import parsers
from parsers.device import _devices_parser, _device_parser

device_ns = Namespace('device', 'Device methods')


@device_ns.route('/')
class Devices(Resource):
    """
    Shows a list of devices, and lets you POST to add new device
    """
    @device_ns.doc(
        responses={
            200: "Add successful.",
            400: "Add unsuccessful.",
        },
        parser=_devices_parser
    )
    def post(self):
        """Add new device"""
        data = _devices_parser.parse_args()

        # create new device
        new_device = DeviceModel()
        new_device._set(data)

        try:
            new_device.save()
            return {"message": "Device added successfully."}, 200
        except:
            return {"message": "Adding device unsuccessful. Please try again."}, 400

    @device_ns.doc(
        response={
            200: "Get all devices successful.",
            400: "Get all devices unsuccessful.",
        }
    )
    def get(self):
        """Get all devices"""
        try:
            data = DeviceModel.objects.all()
            # serialize
            devices = [device.json() for device in data]
            return {"message": "Get all devices successful", "data": devices}, 200
        except:
            return {"message": "Get all devices unsuccessful. Please try again."}, 400


@device_ns.route('/detail')
class Device(Resource):
    """
    Shows detail about a device, and lets you DELETE, PUT a device
    """
    @device_ns.doc(
        parser=_device_parser,
        responses={
            200: "Get all devices successful.",
            400: "Get all devices unsuccessful.",
        }
    )
    def get(self):
        """Get detail about a device"""
        data = _device_parser.parse_args()
        try:
            device = DeviceModel.objects(_id=data['id']).first()
            return {"message": "Get all devices successful", "data": device.json()}, 200
        except:
            return {"message": "Get all devices unsuccessful. Please try again."}, 400

    @device_ns.doc(
        parser=_device_parser,
        responses={
            200: "Update device successful.",
            400: "Update device unsuccessful.",
        }
    )
    def put(self):
        data = _device_parser.parse_args()
        try:
            device = DeviceModel.objects(_id=data['id']).first()
            device._update(data)
            device.save()
            return {"message": "Update device successful.", "data": device.json()}, 200

        except Exception as e:
            print(e)
            return {"message": "Update device unsuccessful."}, 400

    @device_ns.doc(
        parser=_device_parser,
        responses={
            200: "Delete device successful.",
            400: "Delete device unsuccessful.",
        }
    )
    def delete(self):
        data = _device_parser.parse_args()
        try:
            device = DeviceModel.objects(_id=data['id']).first()
            device._delete()
            return {"message": "Delete device successful."}, 200

        except:
            return {"message": "Delete device unsuccessful."}, 400
