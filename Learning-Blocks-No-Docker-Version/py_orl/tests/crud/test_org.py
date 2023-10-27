from sqlalchemy.orm import Session

import crud
from schemas.org import OrgCreate
from tests.utils.utils import random_lower_string, random_source_id


def test_create_org(db: Session) -> None:
    """
    Test create org in the database.
    """
    name = random_lower_string()
    source_id = random_source_id()
    org_in = OrgCreate(name=name, sourceId=source_id)
    org = crud.org.create(db=db, obj_in=org_in)
    assert org.name == name
    assert org.sourceId == source_id


def test_get_org(db: Session) -> None:
    """
    Test get org in the database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name, sourceId=random_source_id())
    org = crud.org.create(db=db, obj_in=org_in)
    stored_org = crud.org.get_by_sourceId(db=db, sourceId=org.sourceId)
    assert stored_org
    assert org.sourceId == stored_org.sourceId
    assert org.name == stored_org.name


def test_update_org(db: Session) -> None:
    """
    Test update org in the database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name, sourceId=random_source_id())
    org = crud.org.create(db=db, obj_in=org_in)
    name2 = random_lower_string()
    # This is the testing using the same source id, which should probably fail.
    org_in2 = OrgCreate(name=name2, sourceId=2)
    org2 = crud.org.create(db=db, obj_in=org_in2)
    assert org.sourceId != org2.sourceId
    assert org.name != org2.name


def test_delete_org(db: Session) -> None:
    """
    Test deleting orgs in the database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name, sourceId=random_source_id())
    org = crud.org.create(db=db, obj_in=org_in)
    org2 = crud.org.remove(db=db, id=org.id)
    org3 = crud.org.get(db=db, id=org.id)
    assert org3 is None
    assert org2.sourceId == org.sourceId
