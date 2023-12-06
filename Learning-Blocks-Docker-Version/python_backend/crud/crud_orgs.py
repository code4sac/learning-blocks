from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.orgs import Orgs
from schemas.orgs import OrgsCreate, OrgsUpdate


class CRUDOrgs(CRUDBase[Orgs, OrgsCreate, OrgsUpdate]):
    def create_with_sourcedId(
            self, db: Session, *, obj_in: OrgsCreate, sourcedId: str
    ) -> Orgs:
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
            self, db: Session, *, sourcedId: str
    ) -> Orgs:
        """
        Get org by sourcedId.
        """
        return (
            db.query(self.model)
            .filter(self.model.sourcedId == sourcedId)
            .first()
        )


orgs = CRUDOrgs(Orgs)
