import jwt
from datetime import datetime,timedelta,timezone

from pwdlib import PasswordHash
password_hash=PasswordHash.recommended()

def hash_password(password:str)->str:
    return password_hash.hash(password)

def verify_password(password:str,hashed_password:str)->bool:
    return password_hash.verify(password,hashed_password)

SECRET_KEY="ciQ8WDianwFBM-ss9whkGLQ6QONwiGJPyCgwf7HGZKs"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token