from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

from app.models import Water_Status

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class ArduinoData(BaseModel):
    humidity: int
    temperature: int

    class Config:
        orm_mode = True

class Test(BaseModel):
    humidity: str

    class Config:
        orm_mode = True

class WaterStatus(BaseModel):
    water_status: int
    camera_id: int

    class Config:
        orm_mode = True

class WaterStatusOut(BaseModel):
    camera_id: int
    water_status: int
    created_at: datetime

    class Config:
        orm_mode = True

