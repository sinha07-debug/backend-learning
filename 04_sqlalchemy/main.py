from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas

from db import get_db
from crud import get_games, get_game

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Game Store API"}


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"message": "Database session works!"}


@app.get("/games")
def read_games(db: Session = Depends(get_db)):
    return get_games(db)


@app.get("/games/{game_id}")
def read_game(game_id: int, db: Session = Depends(get_db)):

    game = get_game(db, game_id)

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    return game

@app.post("/games",response_model=schemas.GameResponse,status_code=201)
def create_game(
    game:schemas.GameCreate,
    db:Session=Depends(get_db)
):
    return crud.create_game(db,game)

@app.put("/games/{game_id}",response_model=schemas.GameResponse)
def update_game(
    game_id:int,
    game_update:schemas.GameUpdate,
    db:Session=Depends(get_db)
):
    game=crud.update_game(db,game_id,game_update)
    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )
    return game

@app.delete("/games/{game_id}",status_code=204)
def delete_game(
    game_id:int,
    db:Session=Depends(get_db)
):
    game=crud.delete_game(db,game_id)
    if game is None:
        return HTTPException(
            status_code=404,
            detail="Game not found"
        )
