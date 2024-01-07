from sqlalchemy.orm import Session

from crud import orgs
from models.orgs import Orgs
from schemas import OrgsCreate
from tests.utils.utils import random_lower_string


def create_random_org(db: Session) -> Orgs:
    """
    Create a random org object.
    """
    name = random_lower_string()
    org_in = OrgsCreate(name=name, sourcedId=1)
    return orgs.create(db=db, obj_in=org_in)
