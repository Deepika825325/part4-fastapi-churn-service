from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_invalid_payload():

    payload = {
        "city_tier": "Tier 1"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422