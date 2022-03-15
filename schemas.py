from unicodedata import name
from pydantic import BaseModel

class User(BaseModel):
    name: str

class Products(BaseModel):
    name: str
    price: float
    description: str
    img: str

    