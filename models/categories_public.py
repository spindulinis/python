from sqlmodel import SQLModel

from models.category_public import CategoryPublic

class CategoriesPublic(SQLModel):
    data: list[CategoryPublic]
    count: int