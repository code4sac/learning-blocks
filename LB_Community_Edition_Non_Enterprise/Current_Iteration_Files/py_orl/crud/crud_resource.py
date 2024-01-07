
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.resource import Resource
from schemas.resource_schema import ResourceCreate, ResourceUpdate

class CRUDResource(CRUDBase[Resource, ResourceCreate, ResourceUpdate]):

    def create_with_sourcedId(self, db: Session, *, obj_in: ResourceCreate, sourcedId: str) -> Resource:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourcedId=sourcedId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_sourcedId(self, db: Session, *, sourcedId: str) -> Resource:
        return db.query(self.model).filter(self.model.sourcedId == sourcedId).first()

    def get_by_parentSourcedId(self, db: Session, *, parentSourcedId: str) -> Resource:
        return db.query(self.model).filter(self.model.parentSourcedId == parentSourcedId).first()

crud_resource = CRUDResource(Resource)
