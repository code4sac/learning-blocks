from datetime import datetime

from sqlalchemy.orm import Session
from sqlmodel import select

import crud
from core.config import settings
from neworgsmodel import Org, OrgCreate


def init_db(session: Session) -> None:
    """
    Initialize the database.
    Default options can include:
    ```python
       name='First Example School'
    ```
    Tables should be created with Alembic migrations
    But if you don't want to use migrations, create
    the tables use the following line: `Base.metadata.create_all(bind=engine)`
    """
    
    org = session.exec(
        select(Org).where(Org.sourcedId == settings.EXAMPLE_SCHOOL)
    ).first()

    if not org:
        org_in = OrgCreate(
            sourcedId=settings.EXAMPLE_SCHOOL,
            status='Active',
            dateLastModified=f"{datetime.utcnow().timestamp()}",
            name='First Example School',
            type='School',
            identifier='0',         
        )
        db_obj = Org.from_orm(org_in)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    
    # academicsessions = crud.academicsessions.get_by_sourcedId(session, sourcedId=settings.EXAMPLE_SCHOOL)
    # if not academicsessions:
    #     academicsession_in = schemas.AcademicsessionsCreate(
    #         sourcedId=settings.EXAMPLE_SCHOOL,
    #         status='active',
    #         title='Sample Academic Session',
    #         type='semester',
    #         parentSourcedId='0',
    #     )
    #     academicsessions = crud.academicsessions.create(db, obj_in=academicsession_in)
