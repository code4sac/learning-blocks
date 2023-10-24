from sqlalchemy.orm import Session

import crud
import schemas
from core.config import settings


def init_db(db: Session) -> None:
    user = crud.org.get_by_email(db, email=settings.first_superuser)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.first_superuser,
            password=settings.first_superuser_password,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)
