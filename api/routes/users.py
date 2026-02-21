from fastapi import APIRouter
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)

from models import (
    User,
    UsersPublic,
)

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UsersPublic)
def read_users(session: SessionDep, skip: int = 0, limit: int = 100):
    """
    Retrieve users.
    """

    count_statement = select(func.count()).select_from(User)
    count = session.exec(count_statement).one()

    statement = (
        select(User).order_by(col(User.created_date).desc()).offset(skip).limit(limit)
    )
    users = session.exec(statement).all()

    return UsersPublic(data=users, count=count)
