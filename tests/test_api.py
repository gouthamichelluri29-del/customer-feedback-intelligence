from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_feedback_endpoint():
    response = client.post(
        "/feedback/analyse",
        json = {
            "feedback": "This product is terrible and completely broken"
        },
    )
    assert response.status_code == 200

    data = response.json()
    assert "sentiment" in data
    assert "category" in data
    assert "priority" in data


def test_feedback_validation():
    response = client.post(
        "/feedback/analyse",
        json={
            "feedback": ""
        },
    )

    assert response.status_code == 422