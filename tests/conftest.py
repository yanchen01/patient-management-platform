import pytest

from app import app as flask_app


@pytest.fixture
def app():
    flask_app.config['MONGODB_SETTINGS'] = {
        'db': 'patient-management-test',
        'host': 'mongodb://localhost/patient-management-test'
    }
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
