from sqlalchemy.orm import Session
from sqlalchemy import select

import models
import schemas

def get_game(db: Session, game_id: int):
    return db.scalar(
        select(models.Game).where(models.Game.g_id == game_id)
    )


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(
        select(models.Game)
        .offset(skip)
        .limit(limit)
    ).all()

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(**game.model_dump())

    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game

def update_game(
    db: Session,
    game_id: int,
    game_update: schemas.GameUpdate
):
    db_game = get_game(db, game_id)

    if not db_game:
        return None

    update_data = game_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_game, key, value)

    db.commit()
    db.refresh(db_game)
    return db_game

def delete_game(db: Session, game_id: int):
    db_game = get_game(db, game_id)

    if not db_game:
        return None

    db.delete(db_game)
    db.commit()
    return db_game