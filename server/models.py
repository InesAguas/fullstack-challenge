import random

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Text,
    ForeignKey,
    Float,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def random_delay():
    delta =  random.randint(60, 900)
    return datetime.now() + timedelta(seconds=delta)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    hashed_password = Column(Text, nullable=False)

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    

class PlateOrder(Base):
    __tablename__ = 'plate_order'

    plate_id = Column(ForeignKey('plate.plate_id'), primary_key=True)
    order_id = Column(ForeignKey('order.order_id'), primary_key=True)
    quantity = Column(Integer, default=1, nullable=False)
    
    plate = relationship("Plate", back_populates="orders")
    order = relationship("Order", back_populates="plates")


class Plate(Base):
    __tablename__ = "plate"

    plate_id = Column(Integer, primary_key=True)
    plate_name = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    picture = Column(Text)

    orders = relationship("PlateOrder", back_populates="plate")
    reviews = relationship("Review", back_populates="plate")


class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    order_time = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    user_id = Column(ForeignKey('user.user_id'), nullable=False)

    __finish_time = Column(DateTime(timezone=True), default=random_delay, nullable=False)

    plates = relationship("PlateOrder", back_populates="order")
    user = relationship("User", back_populates="orders")


class Review(Base):
    __tablename__ = "review"

    review_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'), nullable=False)
    plate_id = Column(ForeignKey('plate.plate_id'), nullable=False)
    comment = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)

    plate = relationship("Plate", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
    


