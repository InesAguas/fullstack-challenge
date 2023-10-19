from fastapi import APIRouter, Depends

from server.crud.users import add_user, get_user_by_credentials
from server.schemas import User, UserCredentials, UserBase, Token
from server.utils import get_db
from sqlalchemy.orm import Session
from server.dependencies.security import generate_token


router = APIRouter()


@router.post("/registration", response_model=UserBase)
async def registration(item: UserCredentials, db_session=Depends(get_db)):
    """User registration.

    """
    return add_user(db_session, item)

@router.post("/login", response_model=Token)
async def login(item: UserCredentials, db_session=Depends(get_db)):
    """User login.

    """
    user = get_user_by_credentials(db_session, item)
    return generate_token(user)
