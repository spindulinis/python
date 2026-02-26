from datetime import timedelta

from fastapi import APIRouter, HTTPException

from api.deps import (
    SessionDep,
)
from core import security
from crud import user as user_crud
from models.authentication_public import AuthenticationPublic
from models.sign_in import SignIn
from models.user_create import UserCreate

router = APIRouter(prefix="/authentication", tags=["authentication"])

@router.post("/sign-up", response_model=AuthenticationPublic)
def sign_up(*, session: SessionDep, user_in: UserCreate):
    """
    Sign up.
    """
    user = user_crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = user_crud.create_user(session=session, user_create=user_in)
    access_token_expires = timedelta(minutes=60)
    token = security.create_access_token(user.id, expires_delta=access_token_expires)

    return AuthenticationPublic(user=user, accessToken=token)

@router.post("/sign-in", response_model=AuthenticationPublic)
def sign_in(*, session: SessionDep, user_in: SignIn):
    """
    Sign in.
    """
    user = user_crud.get_user_by_email(session=session, email=user_in.email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
        )
    
    verified = security.verify_password(user_in.password, user.password)

    if not verified:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
        )
    
    access_token_expires = timedelta(minutes=60)
    token = security.create_access_token(user.id, expires_delta=access_token_expires)

    return AuthenticationPublic(user=user, accessToken=token)