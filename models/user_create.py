from models.base import UserBase
from sqlmodel import Field


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)