from db import SessionLocal
from crud import delete_game


db = SessionLocal()

deleted_game = delete_game(db, 8)

if deleted_game:
    print("Deleted:", deleted_game.g_id, deleted_game.title)
else:
    print("Game not found")

db.close()