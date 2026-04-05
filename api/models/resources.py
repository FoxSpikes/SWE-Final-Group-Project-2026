from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    resource_idn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_name = Column(String(100), unique=True, nullable=False)
    resource_amount = Column(Integer, index=True, nullable=False, server_default='0')
    unit = Column(String(20), nullable=False)

    recipes = relationship("Recipe", back_populates="resource")
