from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class OrderDetailBase(BaseModel):
    quantity: int


class OrderDetailCreate(OrderDetailBase):
    order_idn: int
    menu_item_idn: int

class OrderDetailUpdate(BaseModel):
    order_idn: Optional[int] = None
    menu_item_idn: Optional[int] = None
    quantity: Optional[int] = None


class OrderDetail(OrderDetailBase):
    order_idn: int
    menu_item_idn: int
    sandwich: Sandwich = None

    class ConfigDict:
        from_attributes = True