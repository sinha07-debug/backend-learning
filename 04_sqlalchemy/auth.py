from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from db import get_db
from models import User
from schemas import UserCreate, UserResponse, UserLogin,Token
from security import hash_password,verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user_data:UserCreate,
    db:Session=Depends(get_db)
):
    statement=select(User).where(
        (User.username==user_data.username)|
        (User.email==user_data.email)
    )
    existing_user=db.scalar(statement)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username or email already exists"
        )
    hashed_password=hash_password(user_data.password)

    new_user=User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=Token)
def login_user(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    statement = select(User).where(
        User.username == user_data.username
    )

    user = db.scalar(statement)

    if user is None or not verify_password(
        user_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    access_token = create_access_token(user.username)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }