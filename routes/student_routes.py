from fastapi import APIRouter, HTTPException, Response, status

from models.student_model import Student, StudentResponse
from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# 1. Create Student
@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student_api(student: Student):

    return create_student(student)


# 2. Read All Students
@router.get(
    "",
    response_model=list[StudentResponse],
    status_code=status.HTTP_200_OK
)
def get_all_students_api():

    return get_all_students()


# 3. Read Student By ID
@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def get_student_api(student_id: int):

    student = get_student_by_id(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# 4. Update Student
@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def update_student_api(student_id: int, student: Student):

    updated_student = update_student(student_id, student)

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


# 5. Delete Student
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student_api(student_id: int):

    deleted = delete_student(student_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return Response(status_code=204)