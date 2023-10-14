from functools import wraps

from starlette.responses import Response

from .database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class RawJSONResponse(Response):
    media_type = "application/json"
