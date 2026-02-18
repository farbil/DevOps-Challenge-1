import pytest
from app import app

def test_home_route_structure():
    tester = app.test_client()
    response = tester.get('/')
    # Kita expect 200 OK
    assert response.status_code == 200
    # Kita expect tipe data JSON
    assert response.is_json