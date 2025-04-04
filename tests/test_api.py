# type: ignore

import os

os.environ["NO_MIDDLEWARE"] = "1"

import pytest
from app import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    os.environ["NO_UPDATE_THREAD"] = "1"
    with TestClient(app) as client:
        yield client


def test_api(client):
    client.get('/api/buildqueue2').raise_for_status()
