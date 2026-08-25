from datetime import date, datetime
from pydantic import BaseModel, Field
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