from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session, joinedload
from models.models import PeopleInDB, StudentInDB, TeacherInDB, RoleEnum
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse, StudentInDBResponse, TeacherInDBResponse, StudentInDBCreate, TeacherInDBCreate, PeopleCreateRequest
from databases.databases import get_db  # Ensure relative import is correct
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from typing import Optional
from pydantic import BaseModel

router = APIRouter()
@router.get("/people/{person_id}", response_model=PeopleInDBResponse)
def read_person(person_id: int, db: Session = Depends(get_db)):
    # Get the person from the database
    person = db.query(PeopleInDB).filter(PeopleInDB.ID == person_id).first()
    
    # Check if the person exists
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    # Construct the response data
    response_person = PeopleInDBResponse(
        ID=person.ID,
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
    
    return response_person






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
            AnonymizedStudentID=person.AnonymizedStudentID if person.AnonymizedStudentID is not None else None,
            AnonymizedStudentNumber=person.AnonymizedStudentNumber if person.AnonymizedStudentNumber is not None else None,
            AnonymizedTeacherID=person.AnonymizedTeacherID if person.AnonymizedTeacherID is not None else None
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
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: possibly a duplicate entry.")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

