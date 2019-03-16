from sqlalchemy import (
    Column, String, Integer
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence

Base = declarative_base()

class Product(Base):
    __tablename__='products'
    id = Column(Integer, Sequence('products_id_seq', start=1, increment=1), primary_key=True) 
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price =  Column(Integer, nullable=False)

