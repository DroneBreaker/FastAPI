from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    price =  Column(Integer)
    description =  Column(String)
    img =  Column(String)