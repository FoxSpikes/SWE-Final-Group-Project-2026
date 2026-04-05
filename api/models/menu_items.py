from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    menu_item_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100), unique=True, nullable=True)
    category_idn = Column(Integer, ForeignKey("food_categories.category_idn"))
    price = Column(DECIMAL(5, 2), nullable=False, server_default='0.0')
    calories = Column(Integer, nullable=False, server_default='0')

    category = relationship("FoodCategory", back_populates="sandwiches")
    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")
