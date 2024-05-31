from datetime import datetime

from sqlalchemy.orm import Session

import crud
import schemas
from core.config import settings


def init_db(db: Session) -> None:
    """
    Initialize the database.
    Default options can include:
    ```python
       name='First Example School'
    ```
    """
    org = crud.orgs.get_by_sourcedId(db, sourcedId=settings.example_school)
    academicsessions = crud.academicsessions.get_by_sourcedId(db, sourcedId=settings.example_school)

    if not org:
        org_in = schemas.OrgsCreate(
            sourcedId=settings.example_school,
            status='active',
            dateLastModified=datetime.utcnow().date(),
            name='First Example School',
            type='school',
            parentSourcedId='0',
        )
        org = crud.orgs.create(db, obj_in=org_in)

    # if not academicsessions:
    #     academicsession_in = schemas.AcademicsessionsCreate(
    #         sourcedId=settings.example_school,
    #         status='active',
    #         title='Sample Academic Session',
    #         type='semester',
    #         parentSourcedId='0',
    #     )
    #     academicsessions = crud.academicsessions.create(db, obj_in=academicsession_in)
