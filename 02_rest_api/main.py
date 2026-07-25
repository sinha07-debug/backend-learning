from fastapi import FastAPI,HTTPException
from models import Game
from database import db
app=FastAPI()

@app.get("/")
def home():
    return{"message":"Welcome to Video Games API"}

@app.get("/games")
def get_games():
    return db

@app.get("/games/{game_id}")
def get_game(game_id:int):
    for game in db:
        if game.id==game_id:
            return game

    raise HTTPException(
        status_code=404,
        detail='game not found'
    )

@app.post("/games/")
def create_game(game:Game):
    db.append(game)
    return game

@app.put("/games/{game_id}")
def update_game(game_id:int,game:Game):
