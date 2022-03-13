BASE_URL = '/api/device'


def test_add_device(app, client):
    """Test adding a device"""
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "abcde",
        "type": "thermometer",
        "date_purchased": "03-10-2022",
        "firmware_version": "a1",
        "serial_num": "abc"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Device added successfully.'


def test_get_device(app, client):
    """Test getting info about a device"""
    # add a device, then get the device
    url = f'{BASE_URL}/'
    data = {
        "id": "abcde",
        "type": "thermometer",
        "date_purchased": "03-10-2022",
        "firmware_version": "a1",
        "serial_num": "abc"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Device added successfully.'

    # get device detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "abcde"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get device successful'
    assert response.json['data']['id'] == 'abcde'


def test_update_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "abcde",
        "type": "thermometer",
        "date_purchased": "03-10-2022",
        "firmware_version": "a1",
        "serial_num": "abc"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Device added successfully.'

    # update the device
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "abcde",
        "type": "scale"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Update device successful.'
    assert response.json['data']['id'] == 'abcde'
    assert response.json['data']['type'] == 'scale'


def test_delete_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "abcde",
        "type": "thermometer",
        "date_purchased": "03-10-2022",
        "firmware_version": "a1",
        "serial_num": "abc"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Device added successfully.'

    # delete the device
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "abcde",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Delete device successful.'

    # get the same device, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "abcde"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Get device unsuccessful. Please try again.'


def test_get_all_devices(app, client):
    """Test getting info about all devices"""
    # add two devices
    url = f'{BASE_URL}/'
    data = {
        "id": "abcde",
        "type": "thermometer",
        "date_purchased": "03-10-2022",
        "firmware_version": "a1",
        "serial_num": "abc"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Device added successfully.'

    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "type": "scale",
        "date_purchased": "03-11-2022",
        "firmware_version": "a1",
        "serial_num": "abc"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Device added successfully.'

    # get devices detail
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get all devices successful.'
    assert isinstance(response.json['data'], list)
