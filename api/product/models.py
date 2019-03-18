from sqlalchemy import (
    Column, String, Integer
)
from sqlalchemy.schema import Sequence
from helpers.database import Base
from utilities.utility import Utility

class Product(Base, Utility):
    __tablename__='products'
    id = Column(Integer, Sequence('products_id_seq', start=1, increment=1), primary_key=True) 
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price =  Column(Integer, nullable=False)

