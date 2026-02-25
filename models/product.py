from datetime import datetime
from typing import List

from sqlalchemy import DateTime
from sqlmodel import Field, Relationship

from models.base import get_datetime_utc
from models.product_base import ProductBase
from models.product_category import ProductCategory

class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    updated_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )

    categories: List["Category"] = Relationship( # type: ignore
        back_populates="products", 
        link_model=ProductCategory
    )