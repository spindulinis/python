from datetime import datetime

from sqlalchemy import DateTime
from sqlmodel import Field

from models.base import get_datetime_utc
from models.user_base import UserBase

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    updated_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )