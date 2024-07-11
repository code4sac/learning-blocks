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

@router.get('/', response_model=List[schemas.PeopleInDBSchema])
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
        lambda: db.query(models.PeopleInDB).offset(skip).limit(limit).all()
    )
    
    # Store data in Redis cache asynchronously
    await asyncio.to_thread(redis_client.set, cache_key, schemas.PeopleInDBSchema.dumps(people))
    
    return people

@router.post('/', response_model=schemas.PeopleInDBSchema)
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
    
    # Invalidate cache
    await asyncio.to_thread(redis_client.delete, 'people:*')
    
    return db_person

@router.put('/{person_id}', response_model=schemas.PeopleInDBSchema)
async def update_person(
    person_id: str, person: schemas.PeopleInDBSchema, db: Session = Depends(get_db)
):
    """
    Update a person asynchronously.
    """
    db_person = await asyncio.to_thread(
        lambda: db.query(models.PeopleInDB).filter(models.PeopleInDB.AnonymizedStudentID == person_id).first()
    )
    if not db_person:
        raise HTTPException(status_code=404, detail='Person not found')

    for key, value in person.dict(exclude_unset=True).items():
        setattr(db_person, key, value)
        
    await asyncio.to_thread(db.commit)
    await asyncio.to_thread(db.refresh, db_person)
    
    # Invalidate cache
    await asyncio.to_thread(redis_client.delete, 'people:*')
    
    return db_person

@router.get('/{person_id}', response_model=schemas.PeopleInDBSchema)
async def read_person(
    person_id: str, db: Session = Depends(get_db)
):
    """
    Get person by ID asynchronously.
    """
    cache_key = f'person:{person_id}'
    
    # Check if data exists in Redis cache asynchronously
    cached_data = await asyncio.to_thread(redis_client.get, cache_key)
    if cached_data:
        return schemas.PeopleInDBSchema.parse_raw(cached_data)
    
    db_person = await asyncio.to_thread(
        lambda: db.query(models.PeopleInDB).filter(models.PeopleInDB.AnonymizedStudentID == person_id).first()
    )
    if not db_person:
        raise HTTPException(status_code=404, detail='Person not found')
    
    # Store data in Redis cache asynchronously
    await asyncio.to_thread(redis_client.set, cache_key, schemas.PeopleInDBSchema.dumps(db_person))
    
    return db_person

@router.delete('/{person_id}', response_model=schemas.PeopleInDBSchema)
async def delete_person(
    person_id: str, db: Session = Depends(get_db)
):
    """
    Delete a person asynchronously.
    """
    db_person = await asyncio.to_thread(
        lambda: db.query(models.PeopleInDB).filter(models.PeopleInDB.AnonymizedStudentID == person_id).first()
    )
    if not db_person:
        raise HTTPException(status_code=404, detail='Person not found')
    
    await asyncio.to_thread(db.delete, db_person)
    await asyncio.to_thread(db.commit)
    
    # Invalidate cache
    await asyncio.to_thread(redis_client.delete, f'person:{person_id}')
    await asyncio.to_thread(redis_client.delete, 'people:*')
    
    return db_person
