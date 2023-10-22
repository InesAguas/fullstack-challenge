from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from server.schemas import PlateBase, Plate, PlateRanking

import server.models as md

def get_plates(db_session: Session):
    return db_session.query(md.Plate).all()


def get_plates_ranking(db_session: Session):
    #added order by rating
    result = db_session.query(
        md.Plate,
        func.count(md.PlateOrder.plate_id).label("order_count"),
        func.avg(md.Review.rating).label("rating")
    )\
        .outerjoin(md.PlateOrder)\
        .outerjoin(md.Review)\
        .group_by(md.Plate.plate_id)\
        .order_by(func.count(md.PlateOrder.plate_id).desc(), func.avg(md.Review.rating))\
        .all()
    
    return [PlateRanking(
        plate_name=plate.plate_name,
        price=plate.price,
        picture=plate.picture,
        plate_id=plate.plate_id,
        order_count=order_count,
        rating= round(rating,2) if rating else 0
    ) for plate, order_count, rating in result]

def add_plate(db_session: Session, item: PlateBase):
    to_fetch = db_session.query(md.Plate).filter(md.Plate.plate_name == item.plate_name)

    if to_fetch.first():
        raise HTTPException(status_code=400, detail="Resource already exists.")

    item = md.Plate(plate_name=item.plate_name, price=item.price, picture=item.picture)

    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    return item
