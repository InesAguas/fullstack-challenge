from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from server.schemas import Review, ReviewBase, User

import server.models as md

def get_reviews_by_plate(db_session: Session, plate_id: int):
    #Return all reviews of a plate
    return db_session.query(md.Review).filter(md.Review.plate_id == plate_id).all()

def get_reviews_by_user(db_session: Session, user_id: int):
    #Return all reviews made by user
    return db_session.query(md.Review).filter(md.Review.user_id == user_id).all()

def add_review(db_session: Session, item: ReviewBase, user: User):
    #Check if plate exists
    plate = db_session.query(md.Plate).filter(md.Plate.plate_id == item.plate_id).first()
    if not plate:
        raise HTTPException(status_code=404, detail="Plate not found.")
    
    #Check if user has ordered the plate
    plate_order = db_session.query(md.PlateOrder).join(md.Order).filter(md.PlateOrder.plate_id == item.plate_id, md.Order.user_id == user.user_id).first()
    if not plate_order:
        raise HTTPException(status_code=403, detail="User has not ordered this plate.")
    
    #Check if user has already reviewed the plate
    review = db_session.query(md.Review).filter(md.Review.plate_id == item.plate_id, md.Review.user_id == user.user_id).first()
    if review:
        raise HTTPException(status_code=409, detail="User has already reviewed this plate.")
    
    item = md.Review(user_id=user.user_id, plate_id=plate.plate_id, comment=item.comment, rating=item.rating)

    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    return item


