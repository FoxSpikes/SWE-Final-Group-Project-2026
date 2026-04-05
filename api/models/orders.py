from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_idn = Column(Integer, ForeignKey("customers.customer_idn"))
    promotion_code = Column(String(20), ForeignKey("promotions.promotion_code"), nullable=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(Integer, nullable=True)
    order_status = Column(String(20), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False, server_default='0.0')

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payment_information = relationship("PaymentInformation", back_populates="order", uselist=False)
    feedbacks = relationship("Feedback", back_populates="order")