from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from enums.user_role import UserRole

class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    role: UserRole = Field(default=UserRole.user, max_length=50)