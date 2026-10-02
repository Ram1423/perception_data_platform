from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_progress_endpoint_returns_404_for_missing_dataset():
    response = client.get("/stats/progress?dataset_id=9999")
    assert response.status_code == 404