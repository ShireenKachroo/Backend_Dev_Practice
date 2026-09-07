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

