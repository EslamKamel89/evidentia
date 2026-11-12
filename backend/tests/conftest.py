from collections.abc import Iterator

import pytest
from evidentia_backend.main import create_app
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture()
def app() -> FastAPI:
    return create_app()

@pytest.fixture()
def client(app:FastAPI)->Iterator[TestClient]:
    with TestClient(app) as client:
        yield client

