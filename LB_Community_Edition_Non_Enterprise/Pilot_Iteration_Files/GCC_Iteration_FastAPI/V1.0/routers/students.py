from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.models import SchoolsInDB
from schemas.schemas import SchoolsInDBCreate, SchoolsInDBResponse
from databases.databases import get_db

router = APIRouter()

@router.post("/schools", response_model=SchoolsInDBResponse)
def create_school(school: SchoolsInDBCreate, db: Session = Depends(get_db)):
    try:
        db_school = SchoolsInDB(
            school_code=school.school_code,
            school_name=school.school_name,
            address=school.address,
            city=school.city,
            state=school.state,
            zip_code=school.zip_code,
            bddemo=school.bddemo.json()
        )
        db.add(db_school)
        db.commit()
        db.refresh(db_school)

        return db_school
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/schools/{school_id}", response_model=SchoolsInDBResponse)
def read_school(school_id: int, db: Session = Depends(get_db)):
    school = db.query(SchoolsInDB).filter(SchoolsInDB.id == school_id).first()
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
        existing_school.school_code = school.school_code
        existing_school.school_name = school.school_name
        existing_school.address = school.address
        existing_school.city = school.city
        existing_school.state = school.state
        existing_school.zip_code = school.zip_code

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

