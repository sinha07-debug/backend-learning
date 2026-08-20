from db import SessionLocal
from crud import get_games


db = SessionLocal()

games = get_games(db)

for game in games:
    print(game.g_id, game.title)

db.close()