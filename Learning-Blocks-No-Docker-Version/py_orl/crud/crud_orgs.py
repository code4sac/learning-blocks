from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.orgs import Orgs
from schemas.orgs import OrgCreate, OrgUpdate


class CRUDOrg(CRUDBase[Orgs, OrgCreate, OrgUpdate]):
    def create_with_sourceId(
            self, db: Session, *, obj_in: OrgCreate, sourceId: int
    ) -> Orgs:
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
    ) -> Orgs:
        """
        Get org by sourceId.
        """
        return (
            db.query(self.model)
            .filter(self.model.sourceId == sourceId)
            .first()
        )


orgs = CRUDOrg(Orgs)
