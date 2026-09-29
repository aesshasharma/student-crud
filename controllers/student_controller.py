from models.student_model import Student


students = []

next_id = 1


# Create Student
def create_student(student: Student):
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "email": student.email,
        "course": student.course,
        "semester": student.semester
    }

    students.append(new_student)
    next_id += 1

    return new_student


# Get All Students
def get_all_students():
    return students


# Get Student By ID
def get_student_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


# Update Student
def update_student(student_id: int, student: Student):
    for index in range(len(students)):
        if students[index]["id"] == student_id:

            students[index] = {
                "id": student_id,
                "name": student.name,
                "email": student.email,
                "course": student.course,
                "semester": student.semester
            }

            return students[index]

    return None


# Delete Student
def delete_student(student_id: int):
    for index in range(len(students)):
        if students[index]["id"] == student_id:
            students.pop(index)
            return True

    return False