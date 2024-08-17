from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.models import PeopleInDB 
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse
from databases.databases import get_db  # Use relative import

router = APIRouter()

@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
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
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/people/{person_id}", response_model=PeopleInDBResponse)
def read_person(person_id: int, db: Session = Depends(get_db)):
    try:
        db_person = db.query(PeopleInDB).filter(PeopleInDB.id == person_id).first()
        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
