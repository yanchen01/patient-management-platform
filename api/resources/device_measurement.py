from flask_restx import Resource, Namespace

# Import models
from models.device_measurement import DeviceMeasurement as DeviceMeasurementModel

# Import parsers
from parsers.device_measurement import _measurements_parser, _measurement_parser, _user_measurements_parser  

measurement_ns = Namespace('measurement', 'Device measurement methods')


@measurement_ns.route('/')
class Measurements(Resource):
    """
    Shows a list of measurements, and lets you POST to add new measurement
    """
    @measurement_ns.doc(
        responses={
            200: "Measurement added successfully.",
            400: "Adding measurement unsuccessful. Please try again.",
        },
        parser=_measurements_parser
    )
    def post(self):
        """Add new measurement"""
        data = _measurements_parser.parse_args()

        # create new measurement
        new_measurement = DeviceMeasurementModel()
        new_measurement._set(data)

        try:
            new_measurement.save()
            return {"message": "Measurement added successfully."}, 200
        except Exception as e:
            print(e)
            return {"message": "Adding measurement unsuccessful. Please try again."}, 400

    @measurement_ns.doc(
        response={
            200: "Get all measurements successful.",
            400: "Get all measurements unsuccessful.",
        }
    )
    def get(self):
        """Get all measurements"""
        try:
            data = DeviceMeasurementModel.objects.all()
            # serialize
            measurements = [measurement.json() for measurement in data]
            return {"message": "Get all measurements successful.", "data": measurements}, 200
        except:
            return {"message": "Get all measurements unsuccessful. Please try again."}, 400


@measurement_ns.route('/detail')
class Measurement(Resource):
    """
    Shows detail about a measurement, and lets you DELETE, PUT a measurement
    """
    @measurement_ns.doc(
        parser=_measurement_parser,
        responses={
            200: "Get measurement successfully.",
            400: "Get measurement unsuccessful.",
        }
    )
    def get(self):
        """Get detail about a measurement"""
        data = _measurement_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(
                _id=data['id']).first()
            return {"message": "Get measurement successful", "data": measurement.json()}, 200
        except:
            return {"message": "Get measurement unsuccessful. Please try again."}, 400

    @measurement_ns.doc(
        parser=_measurement_parser,
        responses={
            200: "Update measurement successful.",
            400: "Update measurement unsuccessful.",
        }
    )
    def put(self):
        """Updates a measurement"""
        data = _measurement_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(
                _id=data['id']).first()
            measurement._update(data)
            measurement.save()
            return {"message": "Update measurement successful.", "data": measurement.json()}, 200
        except:
            return {"message": "Update measurement unsuccessful."}, 400

    @measurement_ns.doc(
        parser=_measurement_parser,
        responses={
            200: "Deleted measurement successful.",
            400: "Deleted measurement unsuccessful.",
        }
    )
    def delete(self):
        """Deletes a measurement"""
        data = _measurement_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(
                _id=data['id']).first()
            measurement._delete()
            return {"message": "Delete measurement successful."}, 200
        except:
            return {"message": "Delete measurement unsuccessful."}, 400


@measurement_ns.route('/user')
class UserMeasurement(Resource):
    """
    Shows detail about a measurement, and lets you DELETE, PUT a measurement
    """
    @measurement_ns.doc(
        parser=_user_measurements_parser,
        responses={
            200: "Get user measurements successfully.",
            400: "Get user measurements unsuccessful.",
        }
    )
    def get(self):
        """Get measurements for a user"""
        data = _user_measurements_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(
                user_id=data['user_id']).all()
            data = [x.json() for x in measurement]
            return {"message": "Get measurement successful", "data": data}, 200
        except:
            return {"message": "Get measurement unsuccessful. Please try again."}, 400
