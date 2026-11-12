
from evidentia_backend.main import create_app
from fastapi.testclient import TestClient


def test_health_endpoint(client:TestClient):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
