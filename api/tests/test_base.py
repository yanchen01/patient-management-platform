def test_base_route(app, client):
    """Test base route homepage to swagger UI"""
    url = '/'
    response = client.get(url)
    assert response.status_code == 302
