import pytest
from api.base_api import BaseAPI

@pytest.fixture
def api_client():
    return BaseAPI()
