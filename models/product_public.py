from datetime import datetime
from models.product_base import ProductBase

class ProductPublic(ProductBase):
    id: int
    created_date: datetime | None = None