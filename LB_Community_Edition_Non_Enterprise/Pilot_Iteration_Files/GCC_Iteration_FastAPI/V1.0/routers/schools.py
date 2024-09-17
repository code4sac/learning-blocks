import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text  # Add this import
from models.models import SchoolsInDB
from schemas.schemas import SchoolsInDBCreate, SchoolsInDBResponse
from databases.databases import get_db
import json  

router = APIRouter()

@router.post("/schools/", response_model=SchoolsInDBResponse)
def create_school(school: SchoolsInDBCreate, db: Session = Depends(get_db)):
    try:

        
        # Create a new School instance
        new_school = SchoolsInDB(
            SchoolCode=school.SchoolCode,
            SchoolName=school.SchoolName,
            Address=school.Address,
            City=school.City,
            State=school.State,
            ZipCode=school.ZipCode,
            GradeLevels=school.GradeLevels,  # Ensure this is stored as a list
            MetaData=json.dumps(school.MetaData.model_dump()) if school.MetaData else None
        )
        
        # Add the new School instance to the session
        db.add(new_school)
        
        # Commit the transaction
        db.commit()
        
        # Refresh to get the new ID
        db.refresh(new_school)
        
        # Deserialize MetaData from JSON string
        response_meta_data = None
        if new_school.MetaData:
            try:
                response_meta_data = json.loads(new_school.MetaData)
            except json.JSONDecodeError as e:
                print(f"Error decoding MetaData: {e}")
                raise HTTPException(status_code=500, detail="Failed to decode MetaData.")
        
        # Construct the response data
        response_school = SchoolsInDBResponse(
            ID=new_school.ID,
            SchoolCode=new_school.SchoolCode,
            SchoolName=new_school.SchoolName,
            Address=new_school.Address,
            City=new_school.City,
            State=new_school.State,
            ZipCode=new_school.ZipCode,
            GradeLevels=new_school.GradeLevels,  # Ensure it's returned as a list
            MetaData=response_meta_data,
            people=[]  # Default for now
        )

        return response_school
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

        
@router.get("/schools/{school_id}", response_model=SchoolsInDBResponse)
def read_school(school_id: int, db: Session = Depends(get_db)):
    school = db.query(SchoolsInDB).filter(SchoolsInDB.ID == school_id).first()
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    
    # Deserialize MetaData from JSON string
    response_meta_data = None
    if school.MetaData:
        try:
            response_meta_data = json.loads(school.MetaData)
        except json.JSONDecodeError as e:
            print(f"Error decoding MetaData: {e}")
            raise HTTPException(status_code=500, detail="Failed to decode MetaData.")
    
    # Construct the response data
    response_school = SchoolsInDBResponse(
        ID=school.ID,
        SchoolCode=school.SchoolCode,
        SchoolName=school.SchoolName,
        Address=school.Address,
        City=school.City,
        State=school.State,
        ZipCode=school.ZipCode,
        GradeLevels=school.GradeLevels,
        MetaData=response_meta_data
    )

    return response_school


@router.put("/schools/{school_id}", response_model=SchoolsInDBResponse)
def update_school(school_id: int, school: SchoolsInDBCreate, db: Session = Depends(get_db)):
    existing_school = db.query(SchoolsInDB).filter(SchoolsInDB.ID == school_id).first()
    
    if not existing_school:
        raise HTTPException(status_code=404, detail="School not found")
    
    try:
        # Directly set GradeLevels as a string
        if school.GradeLevels is not None:
            existing_school.GradeLevels = school.GradeLevels

        # Commit the changes
        db.commit()
        db.refresh(existing_school)

        # Deserialize MetaData if necessary
        response_meta_data = None
        if existing_school.MetaData:
            try:
                response_meta_data = json.loads(existing_school.MetaData)
            except json.JSONDecodeError as e:
                print(f"Error decoding MetaData: {e}")
                raise HTTPException(status_code=500, detail="Failed to decode MetaData.")
        
        # Construct the response
        response_school = SchoolsInDBResponse(
            ID=existing_school.ID,
            SchoolCode=existing_school.SchoolCode,
            SchoolName=existing_school.SchoolName,
            Address=existing_school.Address,
            City=existing_school.City,
            State=existing_school.State,
            ZipCode=existing_school.ZipCode,
            GradeLevels=existing_school.GradeLevels,  # Returned as a string
            MetaData=response_meta_data,
            people=[]  # Assuming you handle this elsewhere
        )

        return response_school
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


