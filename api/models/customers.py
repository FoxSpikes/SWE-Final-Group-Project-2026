from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(11), nullable=False)
    address = Column(String(200), nullable=False)

    orders = relationship("Order", back_populates="customer")
    feedbacks = relationship("Feedback", back_populates="customer")
