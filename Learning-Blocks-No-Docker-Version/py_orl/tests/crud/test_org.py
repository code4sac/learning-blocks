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
    org = crud.orgs.create(db=db, obj_in=org_in)
    assert org.name == name
    assert org.sourcedId == source_id


def test_get_org(db: Session) -> None:
    """
    Test get org in the database.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=random_source_id())
    org = crud.orgs.create(db=db, obj_in=org_in)
    stored_org = crud.orgs.get_by_sourcedId(db=db, sourcedId=org.sourcedId)
    assert stored_org
    assert org.sourcedId == stored_org.sourcedId
    assert org.name == stored_org.name


def test_update_org(db: Session) -> None:
    """
    Test update org in the database.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=random_source_id())
    org = crud.orgs.create(db=db, obj_in=org_in)
    name2 = random_lower_string()
    # This is the testing using the same source id, which should probably fail.
    org_in2 = OrgsCreate(name=name2, sourcedId=2)
    org2 = crud.orgs.create(db=db, obj_in=org_in2)
    assert org.sourcedId != org2.sourcedId
    assert org.name != org2.name


def test_delete_org(db: Session) -> None:
    """
    Test deleting org in the database.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=random_source_id())
    org = crud.orgs.create(db=db, obj_in=org_in)
    org2 = crud.orgs.remove(db=db, id=org.id)
    org3 = crud.orgs.get(db=db, id=org.id)
    assert org3 is None
    assert org2.sourcedId == org.sourcedId
