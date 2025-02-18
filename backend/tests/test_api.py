from fastapi.testclient import TestClient
from app.api.main import app
import os

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_query_endpoint(client):
    # First upload a document
    test_content = "Python is a high-level programming language."
    files = [("files", ("test.txt", test_content.encode(), "text/plain"))]
    upload_response = client.post("/upload", files=files)
    assert upload_response.status_code == 200

    # Then test the query
    query_data = {
        "question": "What is Python?",
        "chat_history": []
    }
    response = client.post("/query", json=query_data)
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "sources" in response.json()

def test_upload_documents(client):
    test_content = "This is a test document."
    files = [("files", ("test.txt", test_content.encode(), "text/plain"))]
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    assert "Successfully processed" in response.json()["message"]