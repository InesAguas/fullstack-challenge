from sqlalchemy.orm import Session
from fastapi import HTTPException
from server.schemas import OrderBase, User, StatusUpdate, Order

import server.models as md


def get_orders(db_session: Session, user: User):
    return db_session.query(md.Order).filter(md.Order.user_id == user.user_id).order_by(md.Order.order_time.desc()).all()


def add_order(db_session: Session, item: OrderBase, user: User):
    # Check if all plates exist.
    plate_ids = [plate.plate_id for plate in item.plates]
    plate_ids_result = db_session.query(md.Plate.plate_id).filter(
        md.Plate.plate_id.in_(plate_ids)
    )
    if plate_ids_result.count() != len(plate_ids):
        raise HTTPException(status_code=404, detail="Plate does not exist.")

    # Check if quantity of each plate is non-negative.
    for plate in item.plates:
        if plate.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be more than 0.")

    order = md.Order(user_id = user.user_id, order_status = "Submitted")
    # Add PlateOrder objects.
    for plate in item.plates:
        plate_order = md.PlateOrder(
            plate_id=plate.plate_id,
            order_id=order.order_id,
            quantity=plate.quantity
        )
        order.plates.append(plate_order)

    db_session.add(order)
    db_session.commit()
    db_session.refresh(order)

    return order


def update_order(db_session: Session, order_id: int, item: StatusUpdate, user: User):
    #Dictionary of valid status transitions
    status_transitions = {
        "Submitted": ["Approved", "Rejected", "Canceled"],
        "Approved": ["In Preparation", "Canceled"],
        "In Preparation": ["In Delivery"],
        "In Delivery": ["Delivered"],
    }

    #Check if order exists
    order = db_session.query(md.Order).filter(md.Order.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")
    
    #Check if user is authorized to update order
    if order.user_id != user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized.")
    
    #Check if status transition is valid
    if item.order_status not in status_transitions[order.order_status]:
        raise HTTPException(status_code=400, detail="Invalid status transition.")
    
    order.order_status = item.order_status
    db_session.commit()
    db_session.refresh(order)
    return order