
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.academic_session import AcademicSession
from schemas.academic_session_schema import AcademicSessionCreate, AcademicSessionUpdate

class CRUDAcademicSession(CRUDBase[AcademicSession, AcademicSessionCreate, AcademicSessionUpdate]):

    def create_with_sourcedId(self, db: Session, *, obj_in: AcademicSessionCreate, sourcedId: str) -> AcademicSession:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourcedId=sourcedId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_sourcedId(self, db: Session, *, sourcedId: str) -> AcademicSession:
        return db.query(self.model).filter(self.model.sourcedId == sourcedId).first()

    def get_by_parentSourcedId(self, db: Session, *, parentSourcedId: str) -> AcademicSession:
        return db.query(self.model).filter(self.model.parentSourcedId == parentSourcedId).first()

crud_academicsession = CRUDAcademicSession(AcademicSession)
