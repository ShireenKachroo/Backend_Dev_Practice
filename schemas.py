from pydantic import BaseModel


class StudentCreate(BaseModel):
    id: int
    name: str
    department_id: int


class StudentUpdate(BaseModel):
    name: str | None = None
    department_id: int | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    department_id: int

    class Config:
        from_attributes = True