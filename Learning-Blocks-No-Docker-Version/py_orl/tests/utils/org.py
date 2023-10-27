from sqlalchemy.orm import Session

from crud import org
from models.org import Org
from schemas import OrgCreate
from tests.utils.utils import random_lower_string


def create_random_org(db: Session) -> Org:
    """
    Create a random org object.
    """
    name = random_lower_string()
    org_in = OrgCreate(name=name, sourceId=1)
    return org.create(db=db, obj_in=org_in)
