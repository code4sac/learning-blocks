from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import asyncio

from app import database, schemas, models, redis_client

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/people/', response_model=List[schemas.PeopleInDBSchema])
async def read_people(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Retrieve people with Redis caching asynchronously.
    """
    cache_key = f'people:{skip}:{limit}'
    
    # Check if data exists in Redis cache asynchronously
    cached_data = await asyncio.to_thread(redis_client.get, cache_key)
    if cached_data:
        return schemas.PeopleInDBSchema.parse_raw(cached_data)
    
    # Fetch data from database asynchronously if not in cache
    people = await asyncio.to_thread(
        db.query(models.PeopleInDB).offset(skip).limit(limit).all
    )
    
    # Store data in Redis cache asynchronously
    await asyncio.to_thread(redis_client.set, cache_key, schemas.PeopleInDBSchema.dumps(people))
    
    return people

@router.post('/people/', response_model=schemas.PeopleInDBSchema)
async def create_person(
    person: schemas.PeopleInDBSchema, db: Session = Depends(get_db)
):
    """
    Create new person asynchronously.
    """
    db_person = models.PeopleInDB(**person.dict())
    db.add(db_person)
    await asyncio.to_thread(db.commit)
    await asyncio.to_thread(db.refresh, db_person)
    return db_person

@router.put('/people/{person_id}', response_model=schemas.PeopleInDBSchema)
async def update_person(
    person_id: str, person: schemas.PeopleInDBSchema, db: Session = Depends(get_db)
):
    """
    Update a person asynchronously.
    """
    db_person = db.query(models.PeopleInDB).filter(models.PeopleInDB.AnonymizedStudentID == person_id).first()
    if db_person:
        for key, value in person.dict(exclude_unset=True).items():
            setattr(db_person, key, value)
        await asyncio.to_thread(db.commit)
        await asyncio.to_thread(db.refresh, db_person)
    return db_person

@router.get('/people/{person_id}', response_model=schemas.PeopleInDBSchema)
async def read_person(
    person_id: str, db: Session = Depends(get_db)
):
    """
    Get person by ID asynchronously.
    """
    db_person = await asyncio.to_thread(
        db.query(models.PeopleInDB).filter(models.PeopleInDB.AnonymizedStudentID == person_id).first
    )
    if db_person is None:
        raise HTTPException(status_code=404, detail='Person not found')
    return db_person

@router.delete('/people/{person_id}', response_model=schemas.PeopleInDBSchema)
async def delete_person(
    person_id: str, db: Session = Depends(get_db)
):
    """
    Delete a person asynchronously.
    """
    db_person = db.query(models.PeopleInDB).filter(models.PeopleInDB.AnonymizedStudentID == person_id).first()
    if db_person:
        db.delete(db_person)
        await asyncio.to_thread(db.commit)
    return db_person
