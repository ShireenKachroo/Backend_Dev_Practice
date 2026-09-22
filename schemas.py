from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Department
from schemas import DepartmentCreate, DepartmentResponse


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    departments = db.query(Department).all()
    return departments


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.post(
    "/",
    response_model=DepartmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_department(
    department_data: DepartmentCreate,
    db: Session = Depends(get_db)
):
    existing_department = (
        db.query(Department)
        .filter(Department.id == department_data.id)
        .first()
    )

    if existing_department:
        raise HTTPException(
            status_code=400,
            detail="Department with this ID already exists"
        )

    existing_name = (
        db.query(Department)
        .filter(Department.name == department_data.name)
        .first()
    )

    if existing_name:
        raise HTTPException(
            status_code=400,
            detail="Department with this name already exists"
        )

    department = Department(
        id=department_data.id,
        name=department_data.name
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department