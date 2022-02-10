import sqlalchemy
from datetime import datetime
from srv.users.db import metadata, engine

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
                         sqlalchemy.Column("username", sqlalchemy.String, index=True),
                         sqlalchemy.Column("email", sqlalchemy.String, index=True),
                         sqlalchemy.Column("password", sqlalchemy.String),
                         sqlalchemy.Column("register_date", sqlalchemy.String, default=datetime.now()))

metadata.create_all(bind=engine)
