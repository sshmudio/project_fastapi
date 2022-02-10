from fastapi.testclient import TestClient
from srv.main import app



client = TestClient(app)



def test_read_main():
    response = client.get('/')
    assert response.status_code == 200








# import json




# from fastapi import Request
# import pytest

# # def test_user_create(q):
# #     tester = {"username": "Igor", "email": "igorworker@gmail.com", "id": 2, "password": "MySuperPasswprd1"}

# #     q.setattr(dbutils, "post")

# #     response = requests.post("http://0.0.0.0:8000/user", data=json.dumps(tester),)
# #     assert response.status_code == 201
# #     assert response.json() == tester


# def test_create_user(request):
#     test_data = {"user_name": "Jonh", "email": "Jonh@gmail.com", "id": 2, "password": "123"}




#     response = Request.post("/users/", data=json.dumps(test_data),)
#     assert response.status_code == 201
#     assert response.json() == test_data
