
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.class_model import Class
from schemas.class_model_schema import ClassCreate, ClassUpdate

class CRUDClass(CRUDBase[Class, ClassCreate, ClassUpdate]):

    def create_with_sourcedId(self, db: Session, *, obj_in: ClassCreate, sourcedId: str) -> Class:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourcedId=sourcedId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_sourcedId(self, db: Session, *, sourcedId: str) -> Class:
        return db.query(self.model).filter(self.model.sourcedId == sourcedId).first()

    def get_by_parentSourcedId(self, db: Session, *, parentSourcedId: str) -> Class:
        return db.query(self.model).filter(self.model.parentSourcedId == parentSourcedId).first()

crud_class = CRUDClass(Class)
