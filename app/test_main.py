from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app from the main.py file

client = TestClient(app)

def test_read_root():
    """Test the root endpoint (GET /)"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
