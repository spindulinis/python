from typing import Any

from sqlmodel import Session

from models.attribute import Attribute
from models.attribute_create import AttributeCreate
from models.attribute_update import AttributeUpdate

def create_attribute(*, session: Session, attribute_create: AttributeCreate) -> Attribute:
    db_obj = Attribute.model_validate(attribute_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def update_attribute(*, session: Session, db_attribute: Attribute, attribute_in: AttributeUpdate) -> Any:
    attribute_data = attribute_in.model_dump(exclude_unset=True)
    extra_data = {}
    db_attribute.sqlmodel_update(attribute_data, update=extra_data)
    session.add(db_attribute)
    session.commit()
    session.refresh(db_attribute)
    return db_attribute