from sqlalchemy.ext.declarative import declarative_base
import databases
import sqlalchemy
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

DEBUG = False

database = databases.Database(DATABASE_URL, min_size=5, max_size=20)
engine = sqlalchemy.create_engine(DATABASE_URL, echo=DEBUG)
Base = declarative_base()

metadata = sqlalchemy.MetaData()
