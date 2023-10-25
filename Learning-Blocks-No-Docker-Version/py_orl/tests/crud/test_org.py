from sqlalchemy.orm import Session

import crud
from schemas.org import OrgCreate, OrgUpdate
from tests.utils.utils import random_lower_string


def test_create_org(db: Session) -> None:
    """
    Test create org in database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name)
    org = crud.org.create_with_org(db=db, obj_in=org_in)
    assert org.name == name


def test_get_org(db: Session) -> None:
    """
    Test get org in database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name)
    org = crud.org.create_with_org(db=db, obj_in=org_in)
    stored_org = crud.org.get(db=db, source_id=org.source_id)
    assert stored_org
    assert org.source_id == stored_org.source_id
    assert org.name == stored_org.name


def test_update_org(db: Session) -> None:
    """
    Test update org in database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name)
    org = crud.org.create_with_org(db=db, obj_in=org_in)
    name2 = random_lower_string()
    org_in2 = OrgCreate(name=name2)
    org2 = crud.org.create_with_org(db=db, obj_in=org_in2)
    assert org.id == org2.id
    assert org.name == org2.name


def test_delete_org(db: Session) -> None:
    """
    Test delete org in database.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name)
    org = crud.org.create_with_org(db=db, obj_in=org_in)
    org2 = crud.org.remove(db=db, id=org.id)
    org3 = crud.org.get(db=db, id=org.id)
    assert org3 is None
    assert org2.source_id == org.source_id
