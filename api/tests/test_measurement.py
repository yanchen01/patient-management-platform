BASE_URL = '/api/measurement'


def test_add_measurement(app, client):
    """Test adding a measurement"""
    # add a measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "1",
        "device_id": "abcde",
        "device_type": "thermometer",
        "user_id": "abc",
        "reading": 97.8,
        "unit": "fahrenheit"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Measurement added successfully.'


def test_get_measurement(app, client):
    """Test getting info about a measurement"""
    # add a measurement, then get the measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "1",
        "device_id": "abcde",
        "device_type": "thermometer",
        "user_id": "abc",
        "reading": 97.8,
        "unit": "fahrenheit"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Measurement added successfully.'

    # get measurement detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "1"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get measurement successful'
    assert response.json['data']['id'] == '1'


def test_update_measurement(app, client):
    # add a measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "1",
        "device_id": "abcde",
        "device_type": "thermometer",
        "user_id": "abc",
        "reading": 97.8,
        "unit": "fahrenheit"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Measurement added successfully.'

    # update the measurement
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "1",
        "reading": 100
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Update measurement successful.'
    assert response.json['data']['id'] == '1'
    assert int(response.json['data']['reading']) == 100


def test_delete_measurement(app, client):
    # add a measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "1",
        "device_id": "abcde",
        "device_type": "thermometer",
        "user_id": "abc",
        "reading": 97.8,
        "unit": "fahrenheit"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Measurement added successfully.'

    # delete the measurement
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "1",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Delete measurement successful.'

    # get the same measurement, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "1"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Get measurement unsuccessful. Please try again.'


def test_get_all_measurements(app, client):
    """Test getting info about all measurements"""
    # add two measurements
    url = f'{BASE_URL}/'
    data = {
        "id": "1",
        "device_id": "abcde",
        "device_type": "thermometer",
        "user_id": "abc",
        "reading": 97.8,
        "unit": "fahrenheit"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Measurement added successfully.'

    url = f'{BASE_URL}/'
    data = {
        "id": "2",
        "device_id": "abcdefg",
        "device_type": "scale",
        "user_id": "abc",
        "reading": 150,
        "unit": "lbs"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Measurement added successfully.'

    # get measurements detail
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get all measurements successful.'
    assert isinstance(response.json['data'], list)
