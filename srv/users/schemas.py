from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=256)


class UserDb(UserSchema):
    id: int

    class Config:
        orm_mode = True
