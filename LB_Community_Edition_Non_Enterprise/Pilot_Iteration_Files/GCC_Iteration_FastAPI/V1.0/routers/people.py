from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from models.models import PeopleInDB
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse, StudentInDBResponse, TeacherInDBResponse, StudentInDBCreate, TeacherInDBCreate
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        # Create a new PeopleInDB instance
        new_person = PeopleInDB(
            FirstName=person.FirstName,
            LastName=person.LastName,
            Role=person.Role,
            SourcedID=person.SourcedID,
            EnabledUser=person.EnabledUser,
            DateLastModified=person.DateLastModified,
            SchoolCode=person.SchoolCode,
            AnonymizedStudentID=person.AnonymizedStudentID,
            AnonymizedStudentNumber=person.AnonymizedStudentNumber,
            AnonymizedTeacherID=person.AnonymizedTeacherID
        )
        
        # Add the new PeopleInDB instance to the session
        db.add(new_person)
        
        # Commit the transaction
        db.commit()
        
        # Refresh to get the new ID
        db.refresh(new_person)
        
        # Construct the response data
        response_person = PeopleInDBResponse(
            ID=new_person.ID,
            FirstName=new_person.FirstName,
            LastName=new_person.LastName,
            Role=new_person.Role,
            SourcedID=new_person.SourcedID,
            EnabledUser=new_person.EnabledUser,
            DateLastModified=new_person.DateLastModified,
            SchoolCode=new_person.SchoolCode,
            AnonymizedStudentID=new_person.AnonymizedStudentID,
            AnonymizedStudentNumber=new_person.AnonymizedStudentNumber,
            AnonymizedTeacherID=new_person.AnonymizedTeacherID
        )

        return response_person
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")