from fastapi import FastAPI
# python -m uvicorn main:app --reload

students = {101: "Shireen", 102: "Anshika", 103: "Dhruvi", 104: "Khushi"}
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
