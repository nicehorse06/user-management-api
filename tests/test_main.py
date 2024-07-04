from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI MongoDB example!"}

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "johndoe@example.com", "age": 30})
    assert response.status_code == 200
    assert "_id" in response.json()
    assert response.json()["_id"] is not None
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "johndoe@example.com"
    assert response.json()["age"] == 30
