
from fastapi.testclient import TestClient
from app.main import app, tasks

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello from Docker!"


def test_create_task():
    tasks.clear()

    response = client.post(
        "/tasks",
        json={"title": "Learn Docker"}
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn Docker"


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_delete_task():
    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"


def test_delete_unknown_task():
    response = client.delete("/tasks/999")

    assert response.status_code == 404
