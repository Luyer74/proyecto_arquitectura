import imp
import os
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin
from movie_class import Movie
from user_class import User
from postgres_uri import PostgresURI


# -- Single Responsibility
# Separated the class get_postgres_uri from models

Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    PostgresURI.get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)

local_session = sessionmaker(autoflush=False,
                             autocommit=False, bind=engine)

# create db session
db = local_session()

# each class is in its one file for better architecture


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    link = Column(String)


class User(UserMixin, Base):

    def get_id(self):
        return (self.user_id)

    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    magic_number = Column(Integer)


def start_mappers():
    Base.metadata.create_all(engine)
