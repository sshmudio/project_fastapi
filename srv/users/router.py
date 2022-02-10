from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request
from srv.users.models import users
from srv.users.schemas import UserCreate, UserUpdate, UserSelect
from databases import Database
from srv.utils.dbutils import get_connection
from srv.utils.passwdhash import create_password_hash
app = APIRouter()


def get_users_insert_dict(user):
    pwhash = create_password_hash(user.password)
    values = user.dict()
    print(user.password)
    values.pop("password")
    values["password"] = pwhash
    print(user.password)
    return values


@app.get("/user-list", response_model=List[UserSelect])
async def user_list(request: Request, database: Database = Depends(get_connection)):
    ''' Получить список всех пользователей '''
    query = users.select()
    return await database.fetch_all(query)


@app.get("/user", response_model=UserSelect)
async def get_user(id: int, database: Database = Depends(get_connection)):
    '''
    Получение пользователей по id
    '''
    query = users.select().where(users.columns.id == id)
    return await database.fetch_one(query)


@app.post("/user", response_model=UserSelect)
async def create_user(user: UserCreate, database: Database = Depends(get_connection)):
    ''' Регистрация новых пользователей '''
    query = users.insert()
    values = get_users_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}


@app.put("/user", response_model=UserSelect)
async def update_user(user: UserUpdate, database: Database = Depends(get_connection)):
    ''' Обновление пользователей'''
    query = users.update().where(users.columns.id == user.id)
    values = get_users_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}


@app.delete("/user")
async def delete_user(user: UserUpdate, database: Database = Depends(get_connection)):
    ''' Удаление пользователей '''
    query = users.delete().where(users.columns.id == user.id)
    ret = await database.execute(query)
    return ret


@app.patch("/user")
async def edit_user(user: UserUpdate, database: Database = Depends(get_connection)):
    ''' Изменение пользователей'''
    query = users.update().where(users.columns.id == user.id)
    ret = await database.execute(query)
    return user