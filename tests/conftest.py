import os
from unittest.mock import patch

from pytest import fixture
from fastapi.testclient import TestClient
from auth_server.app import create_app
from auth_server.config.hashicorp import BaoSecretsManager


@fixture(autouse=True)
def reset_bao_secrets_manager():
    """Reset the BaoSecretsManager singleton before each test."""
    BaoSecretsManager._instance = None
    BaoSecretsManager._initialized = False


@fixture(scope='session')
def mock_env_vars():
    """A fixture to mock environment variables for the test session."""
    mock_vars = {
        'BAO_ADDR': 'http://localhost:8200',
        'BAO_TOKEN': 'dev-token',
        'OPENBAO_SECRETS_PATH': 'test',
        'SQLALCHEMY_POOL_RECYCLE': '3600',
        'SQLALCHEMY_DB_ENGINE': 'sqlite',
        'SQLALCHEMY_DATABASE_NAME': 'babylon',
        'MONGO_DATA_LAKE_NAME': 'mock-babylon-datalake',
        'EMBEDDINGS_COLLECTION_CHROMA': 'mock-babylon-embeddings'
    }
    with patch.dict(os.environ, mock_vars):
        yield


MOCK_SECRETS = {
    'DB_HOST': 'https://mock-host.com',
    'DB_PORT': '5432',
    'DB_USERNAME': 'dummy',
    'DB_PASSWORD': 'dummy',
    'MONGO_DB_HOST': 'https://mock-host.com',
    'MONGO_DB_PORT': '27017',
    'MONGO_DB_USER': 'dummy',
    'MONGO_DB_PASSWORD': 'dummy'
}

@fixture(scope="session")
def fast_api_app(mock_env_vars):
    with patch('auth_server.config.hashicorp.OpenBaoApiClient') as mock_api_client:
        mock_api_client.return_value.read_secret_values.return_value = MOCK_SECRETS
        app = create_app()
        # return TestClient(app)
        return app

@fixture(scope='session')
def app_client(fast_api_app):
    with TestClient(fast_api_app) as client:
        yield client
