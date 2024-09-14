import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text  # Add this import
from models.models import SchoolsInDB
from schemas.schemas import SchoolsInDBCreate, SchoolsInDBResponse
from databases.databases import get_db

router = APIRouter()

@router.post("/schools/", response_model=SchoolsInDBResponse)
def create_school(school: SchoolsInDBCreate, db: Session = Depends(get_db)):
    try:
        # Convert BDDemoModel to JSON string if it exists
        MetaData_json = json.dumps(school.MetaData.model_dump()) if school.MetaData else None  # Replace dict() with model_dump()

        # Insert the school record using raw SQL with quoted identifiers
        query = text("""
        INSERT INTO "schools" ("SchoolCode", "SchoolName", "Address", "City", "State", "ZipCode", "MetaData")
        VALUES (:SchoolCode, :SchoolName, :Address, :City, :State, :ZipCode, :MetaData)
        RETURNING "ID", "SchoolCode", "SchoolName", "Address", "City", "State", "ZipCode", "MetaData"
        """)
        result = db.execute(query, {
            "SchoolCode": school.SchoolCode,
            "SchoolName": school.SchoolName,
            "Address": school.Address,
            "City": school.City,
            "State": school.State,
            "ZipCode": school.ZipCode,
            "MetaData": MetaData_json
        })
        db_school = result.fetchone()
        
        if not db_school:
            raise HTTPException(status_code=500, detail="Failed to create school.")
        
        # Commit the transaction
        db.commit()
        
        # Construct the response data
        response_school = SchoolsInDBResponse(
            ID=db_school[0],
            SchoolCode=db_school[1],
            SchoolName=db_school[2],
            Address=db_school[3],
            City=db_school[4],
            State=db_school[5],
            ZipCode=db_school[6],
            MetaData=json.loads(db_school[7]) if db_school[7] else None
        )

        return response_school
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    

@router.get("/schools/{school_id}", response_model=SchoolsInDBResponse)
def read_school(school_id: int, db: Session = Depends(get_db)):
    school = db.query(SchoolsInDB).filter(SchoolsInDB.ID == school_id).first()
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school


# Update a school
@router.put("/schools/{school_id}", response_model=SchoolsInDBResponse)
def update_school(school_id: int, school: SchoolsInDBCreate, db: Session = Depends(get_db)):
    existing_school = db.query(SchoolsInDB).filter(SchoolsInDB.id == school_id).first()
    if not existing_school:
        raise HTTPException(status_code=404, detail="School not found")
    
    try:
        existing_school.SchoolCode = school.SchoolCode
        existing_school.SchoolName = school.SchoolName
        existing_school.Address = school.Address
        existing_school.City = school.City
        existing_school.State = school.State
        existing_school.ZipCode = school.ZipCode
        existing_school.MetaData = json.dumps(school.MetaData.model_dump()) if school.MetaData else None  # Replace dict() with model_dump()

        db.commit()
        db.refresh(existing_school)

        return existing_school
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


# Delete a school
@router.delete("/schools/{school_id}", response_model=SchoolsInDBResponse)
def delete_school(school_id: int, db: Session = Depends(get_db)):
    school = db.query(SchoolsInDB).filter(SchoolsInDB.id == school_id).first()
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    
    try:
        db.delete(school)
        db.commit()
        return school
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

