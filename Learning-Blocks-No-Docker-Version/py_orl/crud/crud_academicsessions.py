from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.academicsessions import academicsessions
from schemas.academicsessions import academicsessionsCreate, academicsessionsUpdate


class CRUDacademicsessions(CRUDBase[academicsessions, academicsessionsCreate, academicsessionsUpdate]):
    def create_with_sourceId(
            self, db: Session, *, obj_in: academicsessionsCreate, sourceId: int
    ) -> academicsessions:
        """
        Unused, but keeping for documentation.
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourceId=sourceId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_sourceId(
            self, db: Session, *, sourceId: int
    ) -> academicsessions:
        """
        Get org by sourceId.
        """
        return (
            db.query(self.model)
            .filter(self.model.sourceId == sourceId)
            .first()
        )
    def get_by_parentSourcedId(
            self, db: Session, *, parentSourcedId: int
    ) -> academicsessions:
        """
        Get org by parentSourcedId.
        """
        return (
            db.query(self.model)
            .filter(self.model.parentSourcedId == parentSourcedId)
            .first()
        )

academic_sessions = CRUDacademicsessions(academicsessions)
