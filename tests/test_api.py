from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_generate_endpoint():
    data = {
        "prompt": "A detective solves a mysterious case.",
        "genre": "mystery"
    }
    response = client.post("/api/v1/generate", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert "story" in json_data
    assert len(json_data["story"]) > 0
