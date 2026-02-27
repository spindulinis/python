from sqlmodel import Field
from models.user_base import UserBase


class UserCreate(UserBase):
    password: str = Field(
        min_length=8,
        max_length=128,
        description="Password must be between 8-128 characters"
    )