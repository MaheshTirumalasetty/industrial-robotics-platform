from fastapi.testclient import TestClient
from api.manufacturing_api.app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_status_endpoint() -> None:
    response = client.get("/status")
    assert response.status_code == 200
    body = response.json()
    assert body["manufacturing_cell"] == "operational"
    assert body["robot_controller"] == "ready"


def test_metrics_endpoint() -> None:
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "manufacturing_api_up 1" in response.text
