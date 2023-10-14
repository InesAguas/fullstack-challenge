from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from server.schemas import PlateBase, Plate, PlateCount

import server.models as md

def get_plates(db_session: Session):
    return db_session.query(md.Plate).all()


def get_plates_count(db_session: Session):
    result = db_session.query(
        md.Plate,
        func.count(md.PlateOrder.plate_id).label("order_count")
    )\
        .outerjoin(md.PlateOrder)\
        .group_by(md.Plate.plate_id)\
        .order_by(func.count(md.PlateOrder.plate_id).desc())\
        .all()
    return [PlateCount(
        plate_name=plate.plate_name,
        price=plate.price,
        picture=plate.picture,
        plate_id=plate.plate_id,
        order_count=order_count
    ) for plate, order_count in result]


def add_plate(db_session: Session, item: PlateBase):
    to_fetch = db_session.query(md.Plate).filter(md.Plate.plate_name == item.plate_name)

    if to_fetch.first():
        raise HTTPException(status_code=409, detail="Resource already exists.")

    item = md.Plate(plate_name=item.plate_name, price=item.price, picture=item.picture)

    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    return item
