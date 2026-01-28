from utils.config import BASE_URL
from api.endpoints import POSTS

def test_delete_post(api_client):
    response = api_client.delete(BASE_URL + POSTS + "/1")
    assert response.status_code == 200
