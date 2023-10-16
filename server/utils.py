from functools import wraps

from starlette.responses import Response

from .database import SessionLocal

from fastapi import Header

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def is_token_valid(token: str = Header(...)):
    return True

class RawJSONResponse(Response):
    media_type = "application/json"
