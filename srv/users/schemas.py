from datetime import date, datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    id: int
    username: str
    email: str
    password: str


class UserSelect(BaseModel):
    username: str
    email: str
    password: str


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str
    register_date: str
