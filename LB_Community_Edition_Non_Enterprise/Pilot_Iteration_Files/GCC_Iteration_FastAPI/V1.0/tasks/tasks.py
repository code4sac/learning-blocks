from celery.celery_app import celery_app
from sqlalchemy.orm import Session
from models.models import PeopleInDB
from schemas.schemas import PeopleInDBCreate
from databases.databases import SessionLocal

@celery_app.task
def create_person_task(person_data: dict):
    db: Session = SessionLocal()
    try:
        person = PeopleInDBCreate(**person_data)
        
        db_person = PeopleInDB(
            name=person.name,
            age=person.age,
            role=person.role,
            AnonymizedStudentID=person.AnonymizedStudentID,
            AnonymizedStudentNumber=person.AnonymizedStudentNumber,
            AnonymizedCounselorNumber=person.AnonymizedCounselorNumber,
            AnonymizedHomeroomTeacherNumber=person.AnonymizedHomeroomTeacherNumber,
            GraduationCohort=person.GraduationCohort,
            Birthdate=person.Birthdate,
            EnabledUser=person.EnabledUser,
            Grades=person.Grades,
            FamilyKey=person.FamilyKey,
            SectionsIDs=person.SectionsIDs,
            GradebookIDs=person.GradebookIDs,
            DateLastModified=person.DateLastModified
        )
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return {"status": "success", "data": db_person.id}
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {str(e)}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close()
