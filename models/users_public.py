from sqlmodel import SQLModel
from models.user_public import UserPublic

class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int