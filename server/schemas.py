from datetime import datetime
from typing import List, Optional, Any
from enum import Enum

from pydantic.utils import GetterDict
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    class Config:
        orm_mode = True

class UserCredentials(UserBase):
    password: str

class User(UserBase):
    user_id: int
    hashed_password: str

class Token(BaseModel):
    token: str
    class Config:
        orm_mode = True

class PlateBase(BaseModel):
    plate_name: str
    price: float
    picture: Optional[str] = None


class Plate(PlateBase):
    plate_id: int

    class Config:
        orm_mode = True

class PlateRanking(Plate):
    order_count: int
    rating: float

    class Config:
        orm_mode = True


class PlateOrderBase(BaseModel):
    plate_id: int
    quantity: int


class PlateOrderGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {'plate_name'}:
            return getattr(self._obj.plate, key)
        else:
            return super(PlateOrderGetter, self).get(key, default)


class PlateOrder(PlateOrderBase):
    plate_name: str
    class Config:
        orm_mode = True
        getter_dict = PlateOrderGetter


class OrderBase(BaseModel):
    plates: List[PlateOrderBase]
    

class Status(str, Enum):
    submitted = 'Submitted',
    approved = 'Approved'
    rejected = 'Rejected'
    canceled = 'Canceled'
    in_preparation = 'In Preparation'
    in_delivery = 'In Delivery'
    delivered = 'Delivered'


class Order(OrderBase):   
    order_id: int
    order_time: datetime
    order_status: Status
    plates: List[PlateOrder]
    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    plate_id: int
    comment: str
    rating: int
    class Config:
        orm_mode = True

class ReviewGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {'username'}:
            return getattr(self._obj.user, key)
        else:
            return super(ReviewGetter, self).get(key, default)

class Review(ReviewBase):
    username: str
    class Config:
        orm_mode = True
        getter_dict = ReviewGetter
