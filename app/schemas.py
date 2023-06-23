from datetime import datetime
from pydantic import BaseModel,EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True



class UserLogin(BaseModel):

    email: EmailStr
    password: str




class PostBase(BaseModel):

    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):

    pass


class Post(BaseModel):

    title: str
    content: str
    published: bool = True
    created_at = datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class Token(BaseModel):

    access_token: str
    token_type: str


class TokenData(BaseModel):

    id: Optional[str] = None
    email: EmailStr