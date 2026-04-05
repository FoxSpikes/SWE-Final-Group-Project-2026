from typing import Optional
from pydantic import BaseModel

from .customers import Customer

class FeedbackBase(BaseModel):
    customer_idn: int
    order_idn: int
    review: str
    stars: int

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackUpdate(BaseModel):
    customer_idn: Optional[int] = None
    order_idn: Optional[int] = None
    review: Optional[str] = None
    stars: Optional[int] = None

class Feedback(FeedbackBase):
    review_idn: int
    customer: Optional[Customer] = None

    class ConfigDict:
        from_attributes = True
