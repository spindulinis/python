from pydantic import EmailStr
from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    role: str = Field(default="user", max_length=50)