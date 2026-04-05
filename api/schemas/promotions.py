from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    promotion_code: str
    expiration_date: datetime
    discount_precentage: int

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    expiration_date: Optional[datetime] = None
    discount_precentage: Optional[int] = None

class Promotion(PromotionBase):
    class ConfigDict:
        from_attributes = True