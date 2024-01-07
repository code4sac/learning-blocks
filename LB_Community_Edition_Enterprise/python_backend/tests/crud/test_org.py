from sqlalchemy.orm import Session

import crud
from schemas.orgs import OrgsCreate
from tests.utils.utils import random_lower_string, random_source_id


def test_create_org(db: Session) -> None:
    """
    Test create org in the database.
    """
    name = random_lower_string()
    source_id = random_source_id()
    org_in = OrgsCreate(name=name, sourcedId=source_id)
    orgs = crud.orgs.create(db=db, obj_in=org_in)
    assert orgs.name == name
    assert orgs.sourcedId == source_id


def test_get_org(db: Session) -> None:
    """
    Test get org in the database.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=random_source_id())
    orgs = crud.orgs.create(db=db, obj_in=org_in)
    stored_org = crud.orgs.get_by_sourcedId(db=db, sourcedId=orgs.sourcedId)
    assert stored_org
    assert orgs.sourcedId == stored_orgs.sourcedId
    assert orgs.name == stored_orgs.name


def test_update_org(db: Session) -> None:
    """
    Test update org in the database.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=random_source_id())
    orgs = crud.orgs.create(db=db, obj_in=org_in)
    name2 = random_lower_string()
    # This is the testing using the same source id, which should probably fail.
    org_in2 = OrgsCreate(name=name2, sourcedId=2)
    org2 = crud.orgs.create(db=db, obj_in=org_in2)
    assert orgs.sourcedId != org2.sourcedId
    assert orgs.name != org2.name


def test_delete_org(db: Session) -> None:
    """
    Test deleting org in the database.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=random_source_id())
    orgs = crud.orgs.create(db=db, obj_in=org_in)
    org2 = crud.orgs.remove(db=db, id=orgs.id)
    org3 = crud.orgs.get(db=db, id=orgs.id)
    assert org3 is None
    assert org2.sourcedId == orgs.sourcedId
