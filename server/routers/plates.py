from fastapi import APIRouter, Depends
from typing import List

from server.crud.plates import get_plates, add_plate, get_plates_count
from server.schemas import PlateBase, Plate, PlateCount
from server.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=List[Plate])
async def search_plates(db_session: Session = Depends(get_db)):
    """Find Plates.

    """
    return get_plates(db_session)


@router.get("/ranking", response_model=List[PlateCount])
async def search_plates_count(db_session: Session = Depends(get_db)):
    """Find the ranked order of plates"""
    return get_plates_count(db_session)


@router.post("", response_model=Plate)
async def post_new_plate(
    item: PlateBase,
    db_session: Session = Depends(get_db),
):
    """Find order by ID.

    """
    return add_plate(db_session, item)
