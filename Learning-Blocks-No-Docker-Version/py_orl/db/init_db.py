from sqlalchemy.orm import Session

import crud
import schemas
from core.config import settings


def init_db(db: Session) -> None:
    """
    Initialize the database.
    Default options can include:
    ```python
       name="First Example School"
    ```
    """
    org = crud.org.get_by_source_id(db, source_id=settings.example_school)
    if not org:
        org_in = schemas.OrgCreate(
            name="First Example School"
        )
        org = crud.org.create(db, obj_in=org_in)
