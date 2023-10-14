from fastapi import APIRouter, Depends
from server.schemas import OrderBase, Order
from server.crud.orders import get_orders, add_order
from server.utils import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.get("", response_model=List[Order])
async def search_orders(db_session: Session = Depends(get_db)):
    """Find order by ID.

    """
    return get_orders(db_session)


@router.post("", response_model=Order)
async def add_new_order(
    item: OrderBase,
    db_session: Session = Depends(get_db)
):
    """Find order by ID.

    """
    return add_order(db_session, item)