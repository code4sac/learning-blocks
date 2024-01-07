from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.academicsessions import Academicsessions
from schemas.academicsessions import AcademicsessionsCreate, AcademicsessionsUpdate


class CRUDAcademicsessions(CRUDBase[Academicsessions, AcademicsessionsCreate, AcademicsessionsUpdate]):
    def create_with_sourcedId(
            self, db: Session, *, obj_in: AcademicsessionsCreate, sourcedId: int
    ) -> Academicsessions:
        """
        Unused, but keeping for documentation.
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourcedId=sourcedId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_sourcedId(
            self, db: Session, *, sourcedId: int
    ) -> Academicsessions:
        """
        Get academic session by sourcedId.
        """
        return (
            db.query(self.model)
            .filter(self.model.sourcedId == sourcedId)
            .first()
        )

    def get_by_parentSourcedId(
            self, db: Session, *, parentSourcedId: int
    ) -> Academicsessions:
        """
        Get academic session by parentSourcedId.
        """
        return (
            db.query(self.model)
            .filter(self.model.parentSourcedId == parentSourcedId)
            .first()
        )


academicsessions = CRUDAcademicsessions(Academicsessions)
