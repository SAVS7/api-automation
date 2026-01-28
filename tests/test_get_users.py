from utils.config import BASE_URL
from api.endpoints import USERS

def test_get_users(api_client):
    response = api_client.get(BASE_URL + USERS)
    assert response.status_code == 200
    assert len(response.json()) > 0
