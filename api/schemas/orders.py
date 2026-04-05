from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from .customers import Customer
from .promotions import Promotion
from .payment_information import PaymentInformation



class OrderBase(BaseModel):
    customer_idn: int
    promotion_code: Optional[str] = None
    tracking_number: Optional[int] = None
    order_status: str
    total_price: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_idn: Optional[int] = None
    promotion_code: Optional[str] = None
    tracking_number: Optional[int] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    order_idn: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    customer: Optional[Customer] = None
    promotion: Optional[Promotion] = None
    payment_information: Optional[PaymentInformation] = None

    class ConfigDict:
        from_attributes = True
