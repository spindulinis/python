from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, func, select

from api.deps import (
    SessionDep,
    get_current_admin_user,
)
from crud import attribute as attribute_crud

from models.base import Message
from models.attribute import Attribute
from models.attribute_create import AttributeCreate
from models.attribute_public import AttributePublic
from models.attribute_update import AttributeUpdate

router = APIRouter(prefix="/attribute", tags=["attribute"])

@router.get("/", response_model=list[AttributePublic], dependencies=[Depends(get_current_admin_user)])
def read_attributes(session: SessionDep):
    """
    Retrieve attributes.
    """

    statement = (
        select(Attribute)
    )
    attributes = session.exec(statement).all()

    return attributes

@router.get("/{attribute_id}", response_model=AttributePublic, dependencies=[Depends(get_current_admin_user)])
def read_category_by_id(attribute_id: int, session: SessionDep):
    """
    Get a specific attribute by id.
    """
    attribute = session.get(Attribute, attribute_id)
    if attribute is None:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return attribute

@router.post("/", response_model=AttributePublic, dependencies=[Depends(get_current_admin_user)])
def create_attribute(*, session: SessionDep, attribute_in: AttributeCreate):
    """
    Create new attribute.
    """
    attribute = attribute_crud.create_attribute(session=session, attribute_create=attribute_in)
    return attribute

@router.patch("/{attribute_id}",response_model=AttributePublic, dependencies=[Depends(get_current_admin_user)])
def update_attribute(*, session: SessionDep, attribute_id: int, attribute_in: AttributeUpdate):
    """
    Update a attribute.
    """

    db_attribute = session.get(Attribute, attribute_id)
    if not db_attribute:
        raise HTTPException(
            status_code=404,
            detail="The attribute with this id does not exist in the system",
        )
    db_attribute = attribute_crud.update_attribute(session=session, db_attribute=db_attribute, attribute_in=attribute_in)
    return db_attribute

@router.delete("/{attribute_id}", dependencies=[Depends(get_current_admin_user)])
def delete_attribute(session: SessionDep, attribute_id: int):
    """
    Delete a attribute.
    """
    attribute = session.get(Attribute, attribute_id)
    if not attribute:
        raise HTTPException(status_code=404, detail="Attribute not found")
    session.delete(attribute)
    session.commit()
    return Message(message="Attribute deleted successfully")