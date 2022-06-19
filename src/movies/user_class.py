from sqlalchemy import Column, Integer, String
from models import Base
from flask_login import UserMixin


# class for User for better and cleaner architecture


class User(UserMixin, Base):

    def get_id(self):
        return (self.user_id)

    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    magic_number = Column(Integer)
