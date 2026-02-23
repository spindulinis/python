from datetime import datetime

from sqlalchemy import DateTime
from sqlmodel import Field

from models.base import UserBase, get_datetime_utc

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )