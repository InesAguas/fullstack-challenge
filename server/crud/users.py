from sqlalchemy.orm import Session
from fastapi import HTTPException
import hashlib
import re

from server.schemas import User, UserCredentials, UserBase, Token

import server.models as md

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(db_session: Session, item: UserCredentials):
    to_fetch = db_session.query(md.User).filter(md.User.username == item.username.lower())

    #Checks if username is already in use
    if to_fetch.first():
        raise HTTPException(status_code=400, detail="Username already in use.")

    #Checks if username is at least 4 characters long and at most 20 characters long
    if len(item.username) < 4 or len(item.username) > 20:
        raise HTTPException(status_code=400, detail="Username must be between 4 and 20 characters long.")
    
    #Checks if password is at least 8 characters long, contains at least 1 number, 1 uppercase letter and 1 lowercase letter
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", item.password):
        raise HTTPException(status_code=400, detail="Password must contain at least 8 characters, 1 number, 1 uppercase letter and 1 lowercase letter.")

    item = md.User(username=item.username.lower(), hashed_password=hash_password(item.password))

    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    return item


def get_user_by_credentials(db_session: Session, item: UserCredentials):
    to_fetch = db_session.query(md.User).filter(md.User.username == item.username.lower())

    if not to_fetch.first():
        raise HTTPException(status_code=400, detail="Wrong credentials.")

    user = to_fetch.first()

    if user.hashed_password != hash_password(item.password):
        raise HTTPException(status_code=400, detail="Wrong credentials.")
    
    return user


def get_user_by_id(db_session: Session, user_id: int):
    to_fetch = db_session.query(md.User).filter(md.User.user_id == user_id)

    if not to_fetch.first():
        raise HTTPException(status_code=404, detail="User not found.")
    
    user = to_fetch.first()
    return user