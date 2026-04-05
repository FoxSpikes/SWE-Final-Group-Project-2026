from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    review_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_idn = Column(Integer, ForeignKey("customers.customer_idn"))
    order_idn = Column(Integer, ForeignKey("orders.order_idn"))
    review = Column(String(1000), nullable=False)
    stars = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="feedbacks")
    order = relationship("Order", back_populates="feedbacks")
