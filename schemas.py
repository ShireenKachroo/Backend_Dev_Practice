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


class DepartmentCreate(BaseModel):
    id: int
    name: str


class DepartmentResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True