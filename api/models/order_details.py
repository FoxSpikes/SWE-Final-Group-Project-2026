from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    order_idn = Column(Integer, ForeignKey("orders.order_idn"), primary_key=True)
    menu_item_idn = Column(Integer, ForeignKey("sandwiches.menu_item_idn"), primary_key=True)
    quantity = Column(Integer, index=True, nullable=False)

    sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
