from db import SessionLocal
from sqlalchemy import select
from models import Game

db = SessionLocal()

stmt = select(Game).where(Game.genre == "RPG")

games = db.scalars(stmt).all()

for game in games:
    print(game.title, game.genre)

db.close()