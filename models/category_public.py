from datetime import datetime
from models.category_base import CategoryBase

class CategoryPublic(CategoryBase):
    id: int
    created_date: datetime | None = None