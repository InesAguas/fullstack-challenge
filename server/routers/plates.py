from fastapi import APIRouter, Depends
from typing import List

from server.crud.plates import get_plates, add_plate, get_plates_ranking
from server.schemas import PlateBase, Plate, PlateRanking
from server.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=List[Plate])
async def search_plates(db_session: Session = Depends(get_db)):
    """Find Plates.

    """
    return get_plates(db_session)


@router.get("/ranking", response_model=List[PlateRanking])
async def search_plates_ranking(db_session: Session = Depends(get_db)):
    """Find the ranked order of plates. The ranking is based on the number of orders and the average rating.
    
    """
    return get_plates_ranking(db_session)


@router.post("", response_model=Plate)
async def post_new_plate(
    item: PlateBase,
    db_session: Session = Depends(get_db),
):
    """Add new plate.

    """
    return add_plate(db_session, item)
