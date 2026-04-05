from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    promotion_code = Column(String(20), primary_key=True, index=True)
    expiration_date = Column(DATETIME, nullable=False)
    discount_precentage = Column(Integer, nullable=False)

    orders = relationship("Order", back_populates="promotion")
