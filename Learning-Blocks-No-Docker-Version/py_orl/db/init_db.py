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
    # academicsession = crud.academicsession.get_by_sourcedId(db, sourcedId=settings.example_school)

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

    # if not academicsession:
    #     academicsession_in = schemas.OrgCreate(
    #         title='Sample Academic Session',
    #         sourcedId=settings.example_school
    #     )
    #     academicsession = crud.academicsession.create(db, obj_in=academicsession_in)
