from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None

