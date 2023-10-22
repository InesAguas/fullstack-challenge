from fastapi import APIRouter, Depends

from server.crud.users import add_user, get_user_by_credentials
from server.schemas import User, UserCredentials, UserBase, Token
from server.utils import get_db
from sqlalchemy.orm import Session
from server.dependencies.security import generate_token


router = APIRouter()


@router.post("/registration", response_model=UserBase)
async def registration(item: UserCredentials, db_session=Depends(get_db)):
    """Endpoint for user registration.
    User has to send the credentials in the body of the request.
    The password is hashed and the user is added to the database.
    """
    return add_user(db_session, item)

@router.post("/login", response_model=Token)
async def login(item: UserCredentials, db_session=Depends(get_db)):
    """Endpoint for user login.
    User has to send the credentials in the body of the request.
    The credentials are checked against the database and if they are correct, a token is generated and returned.

    """
    user = get_user_by_credentials(db_session, item)
    return generate_token(user)
