from fastapi import APIRouter, Depends
from server.schemas import OrderBase, Order, User, StatusUpdate
from server.crud.orders import get_orders, add_order, update_order
from server.utils import get_db
from server.dependencies.security import get_current_user
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.get("", response_model=List[Order])
async def search_orders(db_session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """Get all orders for the user.

    """
    return get_orders(db_session, user)


@router.post("", response_model=Order)
async def add_new_order(
    item: OrderBase,
    db_session: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    """Add new order.

    """
    return add_order(db_session, item, user)


@router.put("/status/{order_id}", response_model=Order)
async def update_order_status(
    order_id: int,
    item: StatusUpdate,
    db_session: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    """Update Order Status.

    """
    return update_order(db_session, order_id, item, user)