from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from .food_categories import FoodCategory

class SandwichBase(BaseModel):
    dish_name: str
    price: float
    category_idn: Optional[int] = None
    calories: int


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    dish_name: Optional[str] = None
    price: Optional[float] = None
    category_idn: Optional[int] = None
    calories: Optional[int] = None


class Sandwich(SandwichBase):
    menu_item_idn: int
    category: Optional[FoodCategory] = None

    class ConfigDict:
        from_attributes = True