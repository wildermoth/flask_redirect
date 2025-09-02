import uuid
from flask import url_for

def test_home_page(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home Page' in response.data

def test_login_redirect(client):
    """Test that the login endpoint redirects to the home page."""
    response = client.get('/login')
    assert response.status_code == 302
    assert response.location == 'http://localhost/'

def test_items_with_query_params(client):
    """Test that query parameters are correctly handled on the items page."""
    response = client.get('/items?category=tools')
    assert response.status_code == 200
    assert b'Items page with category: tools' in response.data

def test_redirect_to_items_with_params(client):
    """Test that a redirect correctly includes query parameters."""
    response = client.get('/redirect-to-items')
    assert response.status_code == 302
    assert response.location == 'http://localhost/items?category=books&sort=asc'

def test_preserve_random_query_params(client):
    # Generate random params
    random_param1: str = str(uuid.uuid4())
    random_param2: str = str(uuid.uuid4())

    # Get both redirect and destination url 
    redirect_url = url_for('preserve_params_redirect', _external=True, p1=random_param1, p2=random_param2)
    destination_url = url_for('destination', _external=True, p1=random_param1, p2=random_param2)

    # Post redirect the response location should be destination url
    response = client.get(redirect_url)

    assert response.status_code == 302
    assert response.location == destination_url

