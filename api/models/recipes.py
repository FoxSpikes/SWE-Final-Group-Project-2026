from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    menu_item_idn = Column(Integer, ForeignKey("sandwiches.menu_item_idn"), primary_key=True)
    resource_idn = Column(Integer, ForeignKey("resources.resource_idn"), primary_key=True)
    recipe_requirement = Column(Integer, index=True, nullable=False, server_default='0')

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")