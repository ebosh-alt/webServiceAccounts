from typing import List, Optional

from pydantic import BaseModel


class Account(BaseModel):
    category: str
    name: str
    description: str
    price: float
    uid: str
    count: int


class Catalog(BaseModel):
    accounts: List[Optional[Account]]


class Message(BaseModel):
    catalog: List[Account]
    status: str


class Response(BaseModel):
    status_code: int
    message: Message
