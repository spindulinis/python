from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from typing import Any
from enums.user_role import UserRole
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    role: UserRole = Field(default=UserRole.user, max_length=50)

    model_config: Any = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True
    )