from sqlalchemy.orm import Session
from srv.users.models import User
from srv.users.schemas import UserSchema
from srv.utils.passwdhash import create_password_hash


class Cruder:
    def post(db_session: Session, payload: UserSchema):
        user = User(username=payload.username, email=payload.email, password=create_password_hash(payload.password))
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user

    def get(db_session: Session, id: int):
        return db_session.query(User).filter(User.id == id).first()

    def get_all(db_session: Session):
        return db_session.query(User).all()

    def put(db_session: Session, user: User, username: str, email: str, password: str):
        user.username = username
        user.email = email
        user.password = create_password_hash(password)
        db_session.commit()
        return user

    def delete(db_session: Session, id: int):
        user = db_session.query(User).filter(User.id == id).first()
        db_session.delete(user)
        db_session.commit()
        return user

# def post(db_session: Session, payload: UserSchema):
#     user = User(username=payload.username, email=payload.email, password=create_password_hash(payload.password))
#     db_session.add(user)
#     db_session.commit()
#     db_session.refresh(user)
#     return user


# def get(db_session: Session, id: int):
#     return db_session.query(User).filter(User.id == id).first()


# def get_all(db_session: Session):
#     return db_session.query(User).all()


# def put(db_session: Session, user: User, username: str, email: str, password: str):
#     user.username = username
#     user.email = email
#     user.password = create_password_hash(password)
#     db_session.commit()
#     return user


# def delete(db_session: Session, id: int):
#     user = db_session.query(User).filter(User.id == id).first()
#     db_session.delete(user)
#     db_session.commit()
#     return user
