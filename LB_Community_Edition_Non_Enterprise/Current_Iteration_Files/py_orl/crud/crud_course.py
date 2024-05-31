
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.course import Course
from schemas.course_schema import CourseCreate, CourseUpdate

class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):

    def create_with_sourcedId(self, db: Session, *, obj_in: CourseCreate, sourcedId: str) -> Course:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, sourcedId=sourcedId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_sourcedId(self, db: Session, *, sourcedId: str) -> Course:
        return db.query(self.model).filter(self.model.sourcedId == sourcedId).first()

    def get_by_parentSourcedId(self, db: Session, *, parentSourcedId: str) -> Course:
        return db.query(self.model).filter(self.model.parentSourcedId == parentSourcedId).first()

crud_course = CRUDCourse(Course)
