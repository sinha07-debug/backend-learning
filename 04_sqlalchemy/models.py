from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column ,relationship
from datetime import date,datetime
from sqlalchemy import (
    String,
    Numeric,
    Text,
    Date,
    ForeignKey,
    CheckConstraint
)
class Base(DeclarativeBase):
    pass

class Developer(Base):
    __tablename__="developers"
    d_id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    country:Mapped[str]=mapped_column(String(50),nullable=False)
    founded_year:Mapped[int] 
    website: Mapped[str | None] = mapped_column(String(255))

    __table_args__=(CheckConstraint("founded_year>1800",name="chk_founded_year"))

    games:Mapped[list["Game"]]=relationship(back_populates="developer")


class Game(Base):
    __tablename__="games"
    g_id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(100),nullable=False)
    genre:Mapped[str]=mapped_column(String(100),nullable=False)
    release_date:Mapped[date]=mapped_column(Date,nullable=False)
    price:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)
    d_id:Mapped[int]=mapped_column(ForeignKey("developers.d_id"),nullable=False)

    __table_args__=(CheckConstraint("price>=0",name="chk_game_price"))

    developer:Mapped["Developer"]=relationship(back_populates="games")
    purchases:Mapped[list["Purchase"]]=relationship(back_populates="game")
    reviews:Mapped[list["Review"]]=relationship(back_populates="game")


class Customer(Base):
    __tablename__="customers"
    c_id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100),nullable=False)
    email: Mapped[str]=mapped_column(String(100),nullable=False,unique=True)

    purchases:Mapped[list["Purchase"]]=relationship(back_populates="customer")
    reviews:Mapped[list["Review"]]=relationship(back_populates="customer")

class Purchase(Base):
    __tablename__ = "purchases"

    p_id: Mapped[int]=mapped_column(primary_key=True)
    c_id: Mapped[int]=mapped_column(ForeignKey("customers.c_id"),nullable=False)
    g_id: Mapped[int]=mapped_column(ForeignKey("games.g_id"),nullable=False)
    p_date: Mapped[datetime | None] = mapped_column(server_default="CURRENT_TIMESTAMP")
    p_price: Mapped[float]=mapped_column(Numeric(10, 2),nullable=False)

    __table_args__ =(CheckConstraint("p_price >= 0",name="chk_purchase_price"),)    

    customer: Mapped["Customer"] = relationship(back_populates="purchases")
    game: Mapped["Game"] = relationship(back_populates="purchases")


class Review(Base):
    __tablename__ = "reviews"

    review_id: Mapped[int] = mapped_column(primary_key=True)
    c_id: Mapped[int] = mapped_column(ForeignKey("customers.c_id"),nullable=False)
    g_id: Mapped[int] = mapped_column(ForeignKey("games.g_id"),nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    comment: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime | None] = mapped_column(server_default="CURRENT_TIMESTAMP")

    __table_args__=(CheckConstraint("rating BETWEEN 1 AND 5",name="chk_review_rating"),)

    customer: Mapped["Customer"] = relationship(back_populates="reviews")
    game: Mapped["Game"] = relationship(back_populates="reviews")