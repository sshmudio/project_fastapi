import pytest
from starlette.testclient import TestClient
from srv.main import app
import json

import pytest

from srv.utils import services


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


def test_create_user_good(test_app, monkeypatch):
    q = {
        "username": "Guido",
        "email": "guido@gmail.com",
        "id": 2,
        "password": "123"
    }

    def mock_post(db_session, payload):
        return q

    monkeypatch.setattr(services, "post", mock_post)

    response = test_app.post("/user/", data=json.dumps(q))
    assert response.status_code == 201
    assert response.json() == q


def test_create_user_fail(test_app):
    response = test_app.post("/user/", data=json.dumps({
        "user": "This fake fail data"
    }))
    assert response.status_code == 422

    response = test_app.post(
        "/user/", data=json.dumps({"username": 0, "email": "", 'password': '123'})
    )
    assert response.status_code == 422


def test_delete_user(test_app, monkeypatch):
    test_data = {"username": "Guido", "email": "guido@gmail.com", "id": 1, 'password': 'SuperPassword'}

    def mock_get(db_session, id):
        return test_data

    monkeypatch.setattr(services, "get", mock_get)

    def mock_delete(db_session, id):
        return test_data

    monkeypatch.setattr(services, "delete", mock_delete)

    response = test_app.delete("/user/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_delete_user_fail(test_app, monkeypatch):
    def mock_get(db_session, id):
        return None

    monkeypatch.setattr(services, "get", mock_get)

    response = test_app.delete("/user/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

    response = test_app.delete("/user/0/")
    assert response.status_code == 422


def test_upd_user_good(test_app, monkeypatch):
    q = {"username": "Guido", "email": "guido@gmail.com", "id": 1, "password": "SuperPassword"}
    upd = {"username": "Brian", "email": "brian@hotmail.com", "id": 1, "password": "easypasswd"}

    def mock_get(db_session, id):
        return q

    monkeypatch.setattr(services, "get", mock_get)

    def mock_put(db_session, user, username, email, password):
        return upd

    monkeypatch.setattr(services, "put", mock_put)

    response = test_app.put("/user/1/", data=json.dumps(upd))
    assert response.status_code == 200
    assert response.json() == upd
