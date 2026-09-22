from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Student
from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)


# Create tables if they don't already exist
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Management API",
    description="FastAPI + PostgreSQL + SQLAlchemy",
    version="1.0.0"
)


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Student Management API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# GET ALL STUDENTS
# --------------------------------------------------

@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    students = db.query(Student).all()

    return students


# --------------------------------------------------
# GET STUDENT BY ID
# --------------------------------------------------

@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# --------------------------------------------------
# FILTER STUDENTS BY DEPARTMENT
# --------------------------------------------------

@app.get(
    "/students/department/{department_id}",
    response_model=list[StudentResponse]
)
def get_students_by_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    students = (
        db.query(Student)
        .filter(Student.department_id == department_id)
        .all()
    )

    return students


# --------------------------------------------------
# CREATE STUDENT
# --------------------------------------------------

@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):

    # Check if ID already exists
    existing_student = (
        db.query(Student)
        .filter(Student.id == student_data.id)
        .first()
    )

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student with this ID already exists"
        )

    student = Student(
        id=student_data.id,
        name=student_data.name,
        department_id=student_data.department_id
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


# --------------------------------------------------
# UPDATE STUDENT
# --------------------------------------------------

@app.patch(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)

    return student


# --------------------------------------------------
# DELETE STUDENT
# --------------------------------------------------

@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return None