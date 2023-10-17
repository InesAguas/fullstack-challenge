from fastapi import APIRouter, Depends
from server.schemas import Review, ReviewBase, User
from server.crud.reviews import get_reviews_by_plate, get_reviews_by_user, add_review
from server.utils import get_db
from server.dependencies.security import get_current_user
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

@router.get("/plate/{plate_id}", response_model=List[Review])
async def search_reviews_by_plate(plate_id: int, db_session: Session = Depends(get_db)):
    """Find reviews by plate.

    """
    return get_reviews_by_plate(db_session, plate_id)

@router.get("", response_model=List[Review])
async def search_reviews_by_user(db_session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """Find reviews by user.

    """
    return get_reviews_by_user(db_session, user.user_id)


@router.post("", response_model=Review)
async def add_new_review(
    item: ReviewBase,
    db_session: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    """Find order by ID.

    """
    return add_review(db_session, item, user)