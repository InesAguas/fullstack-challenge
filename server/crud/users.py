from sqlalchemy.orm import Session
from fastapi import HTTPException
import hashlib

from server.schemas import User, UserCredentials, UserBase, Token

import server.models as md



def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(db_session: Session, item: UserCredentials):
    to_fetch = db_session.query(md.User).filter(md.User.username == item.username)

    if to_fetch.first():
        raise HTTPException(status_code=409, detail="Username already in use.")

    item = md.User(username=item.username, hashed_password=hash_password(item.password))

    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    return item


def get_user_login(db_session: Session, item: UserCredentials):
    to_fetch = db_session.query(md.User).filter(md.User.username == item.username)

    if not to_fetch.first():
        raise HTTPException(status_code=409, detail="Wrong credentials.")

    user = to_fetch.first()

    if user.hashed_password != hash_password(item.password):
        raise HTTPException(status_code=409, detail="Wrong credentials.")
    
    return user


def get_user_by_id(db_session: Session, user_id: int):
    to_fetch = Session.query(md.User).filter(md.User.user_id == user_id)

    if not to_fetch.first():
        raise HTTPException(status_code=404, detail="User not found.")
    
    user = to_fetch.first()
    return user