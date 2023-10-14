from sqlalchemy.orm import Session
from fastapi import HTTPException
from server.schemas import OrderBase

import server.models as md


def get_orders(db_session: Session):
    return db_session.query(md.Order).all()


def add_order(db_session: Session, item: OrderBase):
    # Check if all plates exist.
    plate_ids = [plate.plate_id for plate in item.plates]
    plate_ids_result = db_session.query(md.Plate.plate_id).filter(
        md.Plate.plate_id.in_(plate_ids)
    )
    if plate_ids_result.count() != len(plate_ids):
        raise HTTPException(
            status_code=404,
            detail="Plate does not exist."
        )

    # Check if quantity of each plate is non-negative.
    for plate in item.plates:
        if plate.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Non-positive plate quantity."
            )

    order = md.Order()
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
