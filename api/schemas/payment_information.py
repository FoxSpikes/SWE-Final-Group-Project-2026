from typing import Optional
from pydantic import BaseModel

class PaymentInformationBase(BaseModel):
    order_idn: int
    card_number: Optional[str] = None
    transaction_status: str
    payment_type: str

class PaymentInformationCreate(PaymentInformationBase):
    pass

class PaymentInformationUpdate(BaseModel):
    order_idn: Optional[int] = None
    card_number: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None

class PaymentInformation(PaymentInformationBase):
    payment_idn: int

    class ConfigDict:
        from_attributes = True