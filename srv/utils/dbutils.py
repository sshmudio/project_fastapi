from starlette.requests import Request
from srv.users.db import DbSession


def get_connection(request: Request):
    return request.state.connection


def get_db():
    try:
        db = DbSession()
        yield db
    finally:
        db.close()
