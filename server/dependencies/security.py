from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBearer

from server.schemas import User, UserCredentials, UserBase, Token
from server.crud.users import get_user_by_id
from server.utils import get_db

import hashlib

SECRET_KEY = "your_secret_key"
auth = HTTPBearer()

def generate_token(user: User):
   signature = hashlib.sha256((user.username + SECRET_KEY).encode()).hexdigest()
   return Token(token=f"{user.user_id}:{signature}")


async def get_current_user(db_session=Depends(get_db), token: str = Depends(auth)):
    token = token.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Wrong credentials.")
    parts = token.split(":")
    if len(parts) != 2:
        raise HTTPException(status_code=401, detail="Wrong credentials.")
    
    user_id, signature = parts
    user = get_user_by_id(db_session,user_id)

    if not user:
        raise HTTPException(status_code=401, detail="Wrong credentials.")
    
    if generate_token(user).token != token:
        raise HTTPException(status_code=401, detail="Wrong credentials.")
    
    return user