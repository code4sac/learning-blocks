from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.org import Org
from schemas.org import OrgCreate, OrgUpdate


class CRUDOrg(CRUDBase[Org, OrgCreate, OrgUpdate]):
    def create_with_org(
            self, db: Session, *, obj_in: OrgCreate, org_id: int
    ) -> Org:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, org_id=org_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_org(
            self, db: Session, *, org_id: int, skip: int = 0, limit: int = 100
    ) -> List[Org]:
        return (
            db.query(self.model)
            .filter(Org.org_id == org_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


org = CRUDOrg(Org)
