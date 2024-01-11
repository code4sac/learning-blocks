from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

from crud.base import CRUDBase
from models.org import Org
from schemas.orgs import OrgsCreate, OrgsUpdate


class CRUDOrg(CRUDBase[Org, OrgsCreate, OrgsUpdate]):
    def create_with_sourcedId(
            self, session: Session, *, obj_in: OrgsCreate, sourcedId: str
    ) -> Org:
        """
        Unused, but keeping for documentation.
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourcedId=sourcedId)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def get_by_sourcedId(
            self, session: Session, *, sourcedId: str
    ) -> Org:
        """
        Get org by sourcedId.
        """
        return (
            session.query(self.model)
            .filter(self.model.sourcedId == sourcedId)
            .first()
        )


org = CRUDOrg(Org)
