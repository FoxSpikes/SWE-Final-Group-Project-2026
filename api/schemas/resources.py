from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    resource_name: str
    resource_amount: int
    unit: str


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    resource_name: Optional[str] = None
    resource_amount: Optional[int] = None
    unit: Optional[str] = None


class Resource(ResourceBase):
    resource_idn: int

    class ConfigDict:
        from_attributes = True
