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

def get_developer(db:Session, developer_id:int):
    return db.scalar(
        select(models.Developer).where(
            models.Developer.d_id==developer_id
        )
    )

def get_developers(db: Session):
    return db.scalars(
        select(models.Developer)
    ).all()

def create_developer(db: Session,developer: schemas.DeveloperCreate):
    db_developer = models.Developer(
        **developer.model_dump()
    )

    db.add(db_developer)
    db.commit()
    db.refresh(db_developer)

    return db_developer


def update_developer(
    db: Session,
    developer_id: int,
    developer_update: schemas.DeveloperUpdate
):
    db_developer = get_developer(db, developer_id)

    if not db_developer:
        return None

    update_data = developer_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_developer, key, value)

    db.commit()
    db.refresh(db_developer)

    return db_developer


def delete_developer(db: Session,developer_id: int):
    db_developer = get_developer(db, developer_id)

    if not db_developer:
        return None

    db.delete(db_developer)
    db.commit()

    return
