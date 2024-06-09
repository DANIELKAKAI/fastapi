from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {
            "title": "title 1",
            "description": "description 1",
            "id": 1,
            "owner_id": 1
        },
        {
            "title": "title 11",
            "description": "description 11",
            "id": 2,
            "owner_id": 1
        }
    ]


"""
def test_create_user():
    response = client.post(
        "/users/",
        json={
            "email": "dan2@gmail.com",
            "password": "password"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "email": "dan2@gmail.com",
        "id": 1,
        "is_active": True,
        "items": []
    }
"""
