from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.org import Org
from schemas.org import OrgCreate, OrgUpdate


class CRUDOrg(CRUDBase[Org, OrgCreate, OrgUpdate]):
    def create_with_org(
            self, db: Session, *, obj_in: OrgCreate, source_id: int
    ) -> Org:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, source_id=source_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_source_id(
            self, db: Session, *, source_id: int
    ) -> Org:
        return (
            db.query(self.model)
            .get(source_id)
        )


org = CRUDOrg(Org)
