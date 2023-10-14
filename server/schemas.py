from datetime import datetime
from typing import List, Optional, Any

from pydantic.utils import GetterDict
from pydantic import BaseModel


class PlateBase(BaseModel):
    plate_name: str
    price: float
    picture: Optional[str] = None


class Plate(PlateBase):
    plate_id: int

    class Config:
        orm_mode = True


class PlateCount(Plate):
    order_count: int

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
    

class Order(OrderBase):   
    order_id: int
    order_time: datetime
    plates: List[PlateOrder]

    class Config:
        orm_mode = True
