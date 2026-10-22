from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from decimal import Decimal

class GameCreate(BaseModel):
    title: str
    genre: str
    release_date: date
    price: float = Field(ge=0)
    d_id: int


class GameUpdate(BaseModel):
    title: str | None = None
    genre: str | None = None
    release_date: date | None = None
    price: float | None = Field(default=None, ge=0)
    d_id: int | None = None


class GameResponse(BaseModel):
    g_id: int
    title: str
    genre: str
    release_date: date
    price: float
    d_id: int

    class Config:
        from_attributes = True

class GameBasicResponse(BaseModel):
    g_id: int
    title: str

    class Config:
        from_attributes = True

class DeveloperCreate(BaseModel):
    name: str
    country: str
    founded_year: int
    website: str | None = None


class DeveloperUpdate(BaseModel):
    name: str | None = None
    country: str | None = None
    founded_year: int | None = None
    website: str | None = None


class DeveloperResponse(BaseModel):
    d_id: int
    name: str
    country: str
    founded_year: int
    website: str | None
    games: list[GameBasicResponse]

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    u_id:int
    username:str
    email:EmailStr
    is_active:bool

class UserLogin(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

