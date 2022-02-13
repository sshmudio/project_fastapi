from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from srv.users.db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(256))
    created_date = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
