from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from srv.utils.services import Cruder
from srv.users.schemas import UserSchema, UserDb
from srv.utils.dbutils import get_db


api = APIRouter()


@api.post("/user/", response_model=UserDb, status_code=201)
async def create_user(*, db: Session = Depends(get_db), payload: UserSchema):
    user = Cruder.post(db_session=db, payload=payload)
    return user


@api.get("/user/{id}/", response_model=UserDb)
async def get_user(*, db: Session = Depends(get_db), id: int = Path(..., gt=0)):
    user = Cruder.get(db_session=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@api.get("/user-list/", response_model=List[UserDb])
async def get_users(db: Session = Depends(get_db)):
    return Cruder.get_all(db_session=db)


@api.put("/user/{id}/", response_model=UserDb)
async def update_user(*, db: Session = Depends(get_db), id: int = Path(..., gt=0), payload: UserSchema):
    user = Cruder.get(db_session=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = Cruder.put(
        db_session=db, user=user, username=payload.username, email=payload.email, password=payload.password)
    return user


@api.delete("/user/{id}/", response_model=UserDb)
async def delete_user(*, db: Session = Depends(get_db), id: int = Path(..., gt=0)):
    user = Cruder.get(db_session=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = Cruder.delete(db_session=db, id=id)
    return user
