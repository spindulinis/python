from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
)
from crud import attribute as attribute_crud

from models.attribute import Attribute
from models.attribute_public import AttributePublic
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

@router.get("/{attribute_id}", response_model=AttributePublic)
def read_category_by_id(attribute_id: int, session: SessionDep):
    """
    Get a specific attribute by id.
    """
    attribute = session.get(Attribute, attribute_id)
    if attribute is None:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return attribute