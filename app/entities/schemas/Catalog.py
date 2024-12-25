from typing import List

from pydantic import BaseModel


class Account(BaseModel):
    category: str
    name: str
    description: str
    price: float
    uid: str
    amount: int


class Catalog(BaseModel):
    accounts: List[Account]
