from fastapi import FastAPI
from srv.users.db import database
from srv.users.router import app as route
from starlette.requests import Request

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await database.connect()


@app.on_event("shutdown")
async def shut_down():
    await database.disconnect()
app.include_router(route)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response
