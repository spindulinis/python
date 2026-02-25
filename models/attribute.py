from typing import List

from sqlmodel import Field, Relationship
from models.attribute_base import AttributeBase
from models.product_attribute import ProductAttribute

class Attribute(AttributeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    products: List["Product"] = Relationship( # type: ignore
        back_populates="attributes", 
        link_model=ProductAttribute
    )