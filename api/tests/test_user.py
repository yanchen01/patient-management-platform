BASE_URL = '/api/user'


def test_add_user(app, client):
    """Test adding a user"""
    # add a user
    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "first_name": "yan",
        "last_name": "chen",
        "email": "ychen@gmail.com",
        "password": "test123",
        "user_role": "patient",
        "gender": "male",
        "date_of_birth": "11-16-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 21
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'


def test_get_user(app, client):
    """Test getting info about a user"""
    # add a user, then get the user
    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "first_name": "yan",
        "last_name": "chen",
        "email": "ychen@gmail.com",
        "password": "test123",
        "user_role": "patient",
        "gender": "male",
        "date_of_birth": "11-16-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 21
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'

    # get device detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "abc"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get user successful'
    assert response.json['data']['id'] == 'abc'


def test_update_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "first_name": "yan",
        "last_name": "chen",
        "email": "ychen@gmail.com",
        "password": "test123",
        "user_role": "patient",
        "gender": "male",
        "date_of_birth": "11-16-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 21
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'

    # update the device
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "abc",
        "first_name": "yanyan"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Update user successful.'
    assert response.json['data']['id'] == 'abc'
    assert response.json['data']['first_name'] == 'yanyan'


def test_delete_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "first_name": "yan",
        "last_name": "chen",
        "email": "ychen@gmail.com",
        "password": "test123",
        "user_role": "patient",
        "gender": "male",
        "date_of_birth": "11-16-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 21
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'

    # delete the device
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "abc",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Delete user successful.'

    # get the same device, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "abc"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Get user unsuccessful. Please try again.'


def test_get_all_devices(app, client):
    """Test getting info about all users"""
    # add two devices
    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "first_name": "yan",
        "last_name": "chen",
        "email": "ychen@gmail.com",
        "password": "test123",
        "user_role": "patient",
        "gender": "male",
        "date_of_birth": "11-16-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 21
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'

    url = f'{BASE_URL}/'
    data = {
        "id": "abcde",
        "first_name": "chen",
        "last_name": "yan",
        "email": "cheny@gmail.com",
        "password": "test123",
        "user_role": "doctor",
        "gender": "male",
        "date_of_birth": "11-20-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 22
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'

    # get devices detail
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get all users successful.'
    assert isinstance(response.json['data'], list)


def test_check_user_password(app, client):
    """Test getting info about a user"""
    # add a user, then get the user
    url = f'{BASE_URL}/'
    data = {
        "id": "abc",
        "first_name": "yan",
        "last_name": "chen",
        "email": "ychen@gmail.com",
        "password": "test123",
        "user_role": "patient",
        "gender": "male",
        "date_of_birth": "11-16-2000",
        "address": "33 Harry Agganis Way, Boston 02215",
        "age": 21
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'User added successfully.'

    # get device detail
    url = f'{BASE_URL}/login'
    response = client.get(url, query_string={
        "id": "abc",
        "password": "test123"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'User login successfully.'
