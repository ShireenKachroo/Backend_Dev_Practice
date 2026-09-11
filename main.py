from fastapi import FastAPI
from fastapi import HTTPException  ## HTTP EXCEPTION CODES IN FAST API

# python -m uvicorn main:app --reload

students = {101: {"name": "Shireen", "department": "CSE"}, 102: {"name": "Anshika", "department": "ECE"}, 103: {"name": "Dhruvi", "department": "AI/ML"}, 104: {"name": "Khushi", "department": "DS"}}
app = FastAPI()
@app.get("/")
def print_conn():
    return {"message": "API chal gayi balle balle"}

@app.get("/students")
def get_students():
    return {"students": students}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return {"student": students[student_id]}
    else:
        raise HTTPException(status_code = 404 , detail = "Student not found")

@app.get("/students/department/{department}")
def get_students_by_department(department: str):
    filtered_students = {id: info for id, info in students.items() if info["department"].lower() == department.lower()}
    if filtered_students:
        return {"students": filtered_students}
    else:
        raise HTTPException(status_code = 404, detail = "Department not found!")
# pydantic class for student
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    department: str

@app.post("/students", status_code = 201)
def add_student(student_data: Student):
    new_student_id = max(students.keys()) + 1
    students[new_student_id] = student_data.model_dump()
    return {"message": "Student added", "student_id": new_student_id}

# REQUEST VALIDATION:
# client ---> JSON ---> Pydantic request model ---> Validation ---> your function
# RESPONSE MODELS:
# your function ---> Pydantic Response Model ---> validated/structured response ---> client
class StudentResponse(BaseModel):
    id: int
    name: str
    department: str
@app.post("/students/response", response_model=StudentResponse)
def add_student_response(student_data: Student):
    new_student_id = max(students.keys()) + 1
    students[new_student_id] = student_data.model_dump()
    return StudentResponse(id=new_student_id, name=student_data.name, department=student_data.department)

# PATCH in HTTP
from typing import Optional

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None


@app.patch("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student_data: StudentUpdate):

    # 1. Check if student exists
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # 2. Check whether user actually sent anything
    if not student_data.model_dump(exclude_unset=True):
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    # 3. Update only the fields that were sent
    update_data = student_data.model_dump(exclude_unset=True)

    students[student_id].update(update_data)

    # 4. Return updated student
    return {
        "id": student_id,
        **students[student_id]
    }

## HTTP DELETE METHOD
@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        raise HTTPException(status_code = 404, detail = "Student not found!")
    else:
        del students[student_id]
        return {"message: Student deleted successfully!"}


## DEPENDENCY INJECTION
from fastapi import Depends

def get_current_user():
    return "Shireen"

@app.get("/profile")
def getProfile(user = Depends(get_current_user)):
    return user

## middleware
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(request.method, request.url)

    response = await call_next(request)

    return response

# BASIC AUTHENTICATION IN FASTAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
security = HTTPBasic()

@app.get("/protected")
def protected(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "Shireen" or credentials.password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return {"message": "Welcome Shireen!"}