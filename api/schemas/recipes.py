from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich


class RecipeBase(BaseModel):
    recipe_requirement: int


class RecipeCreate(RecipeBase):
    menu_item_idn: int
    resource_idn: int

class RecipeUpdate(BaseModel):
    menu_item_idn: Optional[int] = None
    resource_idn: Optional[int] = None
    recipe_requirement: Optional[int] = None

class Recipe(RecipeBase):
    menu_item_idn: int
    resource_idn: int
    resource: Optional[Resource] = None
    sandwich: Optional[Sandwich] = None

    class ConfigDict:
        from_attributes = True