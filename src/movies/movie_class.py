from sqlalchemy import Column, Integer, String, Float
from models import Base

# class for Movie for better and cleaner architecture


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    link = Column(String)
