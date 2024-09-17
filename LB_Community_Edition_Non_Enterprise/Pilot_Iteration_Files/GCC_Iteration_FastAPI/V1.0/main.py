from fastapi import FastAPI
from routers import people, students, teachers, schools
from databases.databases import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

# Define FastAPI app
app = FastAPI()

# Include routers
app.include_router(people.router, prefix="/api_V1")
app.include_router(students.router, prefix="/api_V1")
#app.include_router(teachers.router)
app.include_router(schools.router, prefix="/api_V1")
