from fastapi import FastAPI,HTTPException,status,Response
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

@app.post("/games/", response_model=Game,status_code=status.HTTP_201_CREATED)
def create_game(game:Game):
    if any(existing_game.id == game.id for existing_game in db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Game with id {game.id} already exists"
        )

    db.append(game)
    return game

@app.put("/games/{game_id}", response_model=Game)
def update_game(game_id:int,game:Game):

    if game.id != game_id:
        game.id=game_id

    for index,existing_game in enumerate(db):
        if game_id==existing_game.id:
            db[index]=game
            return game

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="game not found"
    )

@app.delete("/games/{game_id}")
def delete_game(game_id:int):
    for index,game in enumerate(db):
        if game_id==game.id:
            db.pop(index)
            return Response(
                status_code=status.HTTP_204_NO_CONTENT
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="game not found"
    )
