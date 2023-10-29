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
    org = crud.org.get_by_sourceId(db, sourceId=settings.example_school)
    academicsessions = crud.academicsessions.get_by_sourceId(db, sourceId=settings.example_school)

    if not org:
        org_in = schemas.OrgCreate(
            name="First Example School",
            sourceId=settings.example_school
        )
        org = crud.org.create(db, obj_in=org_in)

    if not academicsessions:
        academicsessions_in = schemas.OrgCreate(
            title="Sample Academic Session",
            sourceId=settings.example_school
        )
        academicsessions = crud.academicsessions.create(db, obj_in=academicsessions_in)
