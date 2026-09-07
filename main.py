from fastapi import FastAPI
# python -m uvicorn main:app --reload

app = FastAPI()
@app.get("/")
def print_conn():
    return {"message": "API chal gayi balle balle"}

