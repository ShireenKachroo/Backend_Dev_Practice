from fastapi import FastAPI
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
        return {"error": "Student not found"}

@app.get("/students/department/{department}")
def get_students_by_department(department: str):
    filtered_students = {id: info for id, info in students.items() if info["department"].lower() == department.lower()}
    if filtered_students:
        return {"students": filtered_students}
    else:
        return {"error": "No students found in this department"} if department == "" else {"error": "Department not found"}

@app.post("/students")
def add_student(student_data: dict):
    new_student_id = max(students.keys()) + 1
    students[new_student_id] = {"name": student_data["name"], "department": student_data["department"]}
    return {"message": "Student added", "student_id": new_student_id}