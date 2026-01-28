from utils.config import BASE_URL
from api.endpoints import POSTS

def test_update_post(api_client):
    payload = {
        "title": "Updated Title"
    }

    response = api_client.put(BASE_URL + POSTS + "/1", payload)
    assert response.status_code == 200
