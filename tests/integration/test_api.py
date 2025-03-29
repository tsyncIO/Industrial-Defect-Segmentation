from fastapi.testclient import TestClient
from steel_defect.api.app import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict")
    assert response.status_code == 422  # Missing file