from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = "payment_information"

    payment_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_idn = Column(Integer, ForeignKey("orders.order_idn"))
    card_number = Column(String(19), nullable=True)
    transaction_status = Column(String(20), nullable=False)
    payment_type = Column(String(20), nullable=False)

    order = relationship("Order", back_populates="payment_information")
