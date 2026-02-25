from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
from crud import attribute as attribute_crud

from models.attribute import Attribute
from models.attributes_public import AttributesPublic


router = APIRouter(prefix="/attribute", tags=["attribute"])

@router.get("/", response_model=AttributesPublic)
def read_attributes(session: SessionDep, skip: int = 0, limit: int = 100):
    """
    Retrieve attributes.
    """

    count_statement = select(func.count()).select_from(Attribute)
    count = session.exec(count_statement).one()

    statement = (
        select(Attribute).offset(skip).limit(limit)
    )
    attributes = session.exec(statement).all()

    return AttributesPublic(data=attributes, count=count)