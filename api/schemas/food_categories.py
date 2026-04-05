from typing import Optional
from pydantic import BaseModel

class FoodCategoryBase(BaseModel):
    category_name: str

class FoodCategoryCreate(FoodCategoryBase):
    pass

class FoodCategoryUpdate(BaseModel):
    category_name: Optional[str] = None

class FoodCategory(FoodCategoryBase):
    category_idn: int

    class ConfigDict:
        from_attributes = True
