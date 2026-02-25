from typing import List, Optional

from sqlmodel import Field, Relationship

from models.category_base import CategoryBase
from models.product import Product
from models.product_category import ProductCategory

class Category(CategoryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    parent: Optional["Category"] = Relationship(
        back_populates="children", 
        sa_relationship_kwargs={"remote_side": "Category.id"}
    )
    
    children: List["Category"] = Relationship(back_populates="parent")

    products: List["Product"] = Relationship(
        back_populates="categories", 
        link_model=ProductCategory
    )