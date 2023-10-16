import databases
import sqlalchemy
from fastapi import FastAPI, Request
from sqlalchemy import Column, Integer, String, Enum, Date, DateTime
from sqlalchemy.orm import declarative_base
from typing import List

DATABASE_URL = 'postgresql://postgres:Jennzilla1%3F@localhost:5432/lb'
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

academic_session_status_enum1 = sqlalchemy.Enum('active', 'tobedeleted', 'inactive', name='enum1')
academic_session_status_enum2 = sqlalchemy.Enum('gradingPeriod', 'semester', 'schoolYear', 'term', name='enum2')

Base = declarative_base()
metadata = sqlalchemy.MetaData()
academicSessions = sqlalchemy.Table(
    "academicSessions",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False),
    Column("dateLastModified", DateTime),
    Column("title", String),
    Column("type", Enum('gradingPeriod', 'semester', 'schoolYear', 'term', name='enum2'), nullable=False),
    Column("startDate", Date),
    Column("endDate", Date),
    Column("parentSourcedId", String(256), primary_key=True, unique=True, nullable=False),
)

classes = sqlalchemy.Table(
    "classes",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False),
    Column("dateLastModified", DateTime),
    Column("title", String, nullable=False),
    Column("grades", String),
    Column("courseSourcedId", String, nullable=False),
    Column("classCode", String),
    Column("classType", Enum('enumeration_values_for_classType', name='enum_classType'), nullable=False),
    Column("location", String),
    Column("schoolSourcedId", String, nullable=False),
    Column("termSourcedIds", String, nullable=False),
    Column("subjects", String),
    Column("subjectCodes", String),
    Column("periods", String),
)
classResources = sqlalchemy.Table(
    "classResources",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("title", String),
    Column("classSourcedId", String, nullable=False),
    Column("resourceSourcedId", String, nullable=False),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/academicSessions/")
async def read_academic_sessions():
    query = AcademicSession.select()
    academic_sessions = await database.fetch_all(query)
    return academic_sessions

@app.post("/academicSessions/")
async def create_academic_session(request: Request):
    data = await request.json()
    query = AcademicSession.insert().values(**data.dict())
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
