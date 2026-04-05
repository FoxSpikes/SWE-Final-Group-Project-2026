from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..dependencies.database import Base

class FoodCategory(Base):
    __tablename__ = "food_categories"

    category_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_name = Column(String(100), nullable=False)

    menu_items = relationship("Sandwich", back_populates="category")
