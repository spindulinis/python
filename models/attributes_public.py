from sqlmodel import SQLModel
from models.attribute_public import AttributePublic

class AttributesPublic(SQLModel):
    data: list[AttributePublic]
    count: int