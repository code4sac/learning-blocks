import databases
import sqlalchemy
from fastapi import FastAPI, Request
from sqlalchemy import Column, Integer, String, Enum, Date, DateTime, Boolean, Float
from sqlalchemy.orm import declarative_base
from typing import List

DATABASE_URL = [insert postgres db]
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

academic_session_status_enum1 = sqlalchemy.Enum('active', 'tobedeleted', 'inactive', name='enum1')
academic_session_status_enum2 = sqlalchemy.Enum('gradingPeriod', 'semester', 'schoolYear', 'term', name='enum2')
enum_status = Enum('active', 'tobedeleted', 'inactive', name='enum_status')
enum_role = Enum('administrator', 'proctor', 'student', 'teacher', name='enum_role')
enum_user = Enum('true','false', name='enum_user')

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
courseResources = sqlalchemy.Table(
    "courseResources",
    metadata,
    Column("sourcedId", String, primary_key=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("title", String),
    Column("courseSourcedId", String, nullable=False),
    Column("resourceSourcedId", String, nullable=False),
)
courses = sqlalchemy.Table(
    "courses",
    metadata,
    Column("sourcedId", String, primary_key=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("schoolYearSourcedId", String),
    Column("title", String, nullable=False),
    Column("courseCode", String),
    Column("grades", String),
    Column("orgSourcedId", String, nullable=False),
    Column("subjects", String),
    Column("subjectCodes", String),
)
enrollments = sqlalchemy.Table(
    "enrollments",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime),
    Column("classSourcedId", String, nullable=False),
    Column("schoolSourcedId", String, nullable=False),
    Column("userSourcedId", String, nullable=False),
    Column("role", Enum('administrator', 'proctor', 'student', 'teacher', name='enum_role')),
    Column("primary", Boolean),  # Define as a Boolean type
    Column("beginDate", Date),
    Column("endDate", Date),
)
lineItems = sqlalchemy.Table(
    "line_items",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("title", String, nullable=False),
    Column("description", String),
    Column("assignDate", Date, nullable=False),
    Column("dueDate", Date, nullable=False),
    Column("classSourcedId", String, nullable=False),
    Column("categorySourcedId", String, nullable=False),
    Column("gradingPeriodSourcedId", String, nullable=False),
    Column("resultValueMin", Float, nullable=False),
    Column("resultValueMax", Float, nullable=False),
)
orgs = sqlalchemy.Table(
    "orgs",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("name", String, nullable=False),
    Column("type", Enum('enumeration_values_for_type', name='enum_type'), nullable=False),
    Column("identifier", String),
    Column("parentSourcedId", String),
)
resources = sqlalchemy.Table(
    "resources",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("vendorResourceId", String, nullable=False),
    Column("title", String),
    Column("roles", Enum('enumeration_values_for_roles', name='enum_roles')),
    Column("importance", String),
    Column("vendorId", String),
    Column("applicationId", String),
)
results = sqlalchemy.Table(
    "results",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", Enum('active', 'tobedeleted', 'inactive', name='enum_status'), nullable=False),
    Column("dateLastModified", DateTime, nullable=False),
    Column("lineItemSourcedId", String, nullable=False),
    Column("studentSourcedId", String, nullable=False),
    Column("scoreStatus", Enum('enumeration_values_for_scoreStatus', name='enum_scoreStatus'), nullable=False),
    Column("score", Float, nullable=False),
    Column("scoreDate", Date, nullable=False),
    Column("comment", String),
)

users = sqlalchemy.Table(
    "users",
    metadata,
    Column("sourcedId", String(256), primary_key=True, unique=True, nullable=False),
    Column("status", enum_status, nullable=False),  # Use the defined enum_status
    Column("dateLastModified", DateTime, nullable=False),
    Column("enabledUser", enum_user, nullable=False),
    Column("orgSourcedIds", String, nullable=False),
    Column("role", enum_role, nullable=False),  # Use the defined enum_role
    Column("username", String, nullable=False),
    Column("userIds", String),
    Column("givenName", String, nullable=False),
    Column("familyName", String, nullable=False),
    Column("middleName", String),
    Column("identifier", String),
    Column("email", String),
    Column("sms", String),
    Column("phone", String),
    Column("agentSourcedIds", String),
    Column("grades", String),
    Column("password", String),
)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    """
    Database startup event.
    :return: Database session
    """
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    """
    Database shutdown event.
    :return: Database session
    """
    await database.disconnect()

@app.get("/academicSessions/")
async def read_academic_sessions():
    """
    Get all academic sessions.
    :return: Academic sessions
    """
    query = AcademicSession.select()
    academic_sessions = await database.fetch_all(query)
    return academic_sessions

@app.post("/academicSessions/")
async def create_academic_session(request: Request):
    """
    Create a new academic session.
    :param request: Last record ID
    :return:
    """
    data = await request.json()
    query = AcademicSession.insert().values(**data.dict())
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
