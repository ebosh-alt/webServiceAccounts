from typing import List, Optional

from pydantic import BaseModel


class Account(BaseModel):
    category: Optional[str] = ""
    name: Optional[str] = ""
    description: Optional[str] = ""
    price: Optional[float] = ""
    uid: Optional[str] = ""
    count: Optional[int] = 0


class Catalog(BaseModel):
    accounts: Optional[List[Account]] = []


class Message(BaseModel):
    catalog: List[Account]
    status: str
    detail: str


class Response(BaseModel):
    message: Message
