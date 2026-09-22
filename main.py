from fastapi import FastAPI

from database import engine, Base
from routers.students import router as student_router
from routers.departments import router as department_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Management API",
    description="FastAPI + PostgreSQL + SQLAlchemy",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Student Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(student_router)
app.include_router(department_router)