from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
    get_current_admin_user
)
from crud import user as user_crud
from models.base import Message
from models.user import User
from models.user_create import UserCreate
from models.user_public import UserPublic
from models.user_update import UserUpdate
from models.users_public import UsersPublic


router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=UsersPublic, dependencies=[Depends(get_current_admin_user)])
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

@router.get("/{user_id}", response_model=UserPublic, dependencies=[Depends(get_current_admin_user)])
def read_user_by_id(user_id: int, session: SessionDep):
    """
    Get a specific user by id.
    """
    user = session.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserPublic, dependencies=[Depends(get_current_admin_user)])
def create_user(*, session: SessionDep, user_in: UserCreate):
    """
    Create new user.
    """
    user = user_crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = user_crud.create_user(session=session, user_create=user_in)
    return user

@router.patch("/{user_id}",response_model=UserPublic, dependencies=[Depends(get_current_admin_user)])
def update_user(*, session: SessionDep, user_id: int, user_in: UserUpdate):
    """
    Update a user.
    """

    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    db_user = user_crud.update_user(session=session, db_user=db_user, user_in=user_in)
    return db_user

@router.delete("/{user_id}", dependencies=[Depends(get_current_admin_user)])
def delete_user(session: SessionDep, user_id: int):
    """
    Delete a user.
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return Message(message="User deleted successfully")