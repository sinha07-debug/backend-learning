from sqlalchemy.orm import Session
from sqlalchemy import select

import models


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


def create_game(db: Session, game: dict):
    db_game = models.Game(**game)

    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game