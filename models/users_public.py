from sqlmodel import SQLModel
from models.user_public import UserPublic

class UsersPublic(SQLModel):
    items: list[UserPublic]
    total: int
    limit: int
    offset: int