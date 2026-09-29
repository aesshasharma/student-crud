from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str
    email: str
    course: str
    semester: int = Field(..., ge=1, le=12)


class StudentResponse(Student):
    id: int