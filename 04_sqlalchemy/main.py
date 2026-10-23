from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud
import schemas

from db import get_db
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Game Store API"}


@app.get("/games")
def read_games(db: Session = Depends(get_db)):
    return crud.get_games(db)


@app.get("/games/{game_id}")
def read_game(game_id: int, db: Session = Depends(get_db)):

    game = crud.get_game(db, game_id)

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
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

@app.get("/developers",response_model=list[schemas.DeveloperResponse])

def read_developers(db: Session = Depends(get_db)):
    return crud.get_developers(db)

@app.get("/developers/{developer_id}",response_model=schemas.DeveloperResponse)
def read_developer(developer_id:int,db:Session=Depends(get_db)):
    developer=crud.get_developer(db,developer_id)
    if developer is None:
        raise HTTPException(
            status_code=404,
            detail="Developer not found"
        )

    return developer

@app.post("/developers",response_model=schemas.DeveloperResponse,status_code=status.HTTP_201_CREATED)
def create_developer(developer: schemas.DeveloperCreate,db: Session = Depends(get_db)):
    return crud.create_developer(db, developer)

@app.put("/developers/{developer_id}",response_model=schemas.DeveloperResponse)
def update_developer(developer_id: int,developer: schemas.DeveloperUpdate,db: Session = Depends(get_db)):
    updated_developer = crud.update_developer(
        db,
        developer_id,
        developer
    )

    if updated_developer is None:
        raise HTTPException(
            status_code=404,
            detail="Developer not found"
        )

    return updated_developer


@app.delete("/developers/{developer_id}",status_code=204)
def delete_developer(developer_id: int,db: Session = Depends(get_db)):
    developer = crud.delete_developer(
        db,
        developer_id
    )

    if developer is None:
        raise HTTPException(
            status_code=404,
            detail="Developer not found"
        )
    return