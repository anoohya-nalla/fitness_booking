from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_class():
    payload = {"class_id": 1, "client_name": "Tester", "client_email": "tester@gmail.com"}
    response = client.post("/book", json=payload)
    assert response.status_code == 200
    assert response.json()["client_email"] == "tester@gmail.com"

def test_get_bookings():
    response = client.get("/bookings", params={"email": "tester@gmail.com"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
