import pytest
from fastapi.testclient import TestClient
from auth_server.app import create_app

@pytest.fixture(autouse=True, scope='module')
def httpClient():
    app = create_app()
    return TestClient(app)
