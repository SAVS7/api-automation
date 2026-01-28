from utils.config import BASE_URL
from api.endpoints import POSTS

def test_create_post(api_client):
    payload = {
        "title": "API Automation",
        "body": "Testing with PyTest",
        "userId": 1
    }

    response = api_client.post(BASE_URL + POSTS, payload)
    assert response.status_code == 201
    assert response.json()["title"] == "API Automation"
