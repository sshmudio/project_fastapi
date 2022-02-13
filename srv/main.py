from fastapi import FastAPI

from srv.users import routes
from srv.users.models import Base
from srv.users.db import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.api)
