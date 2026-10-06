from typing import List

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from database import Base, engine, get_db

from schemas import (
    StudentCreate,
    StudentResponse
)

from crud import (
    create_student,
    get_students,
    get_student,
    update_student,
    delete_student
)


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Management API",
    description="FastAPI CRUD application using SQLite",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Student Management API is running"
    }


# ------------------------------------------------
# CREATE STUDENT
# ------------------------------------------------

@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student_api(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = create_student(
        db,
        student
    )

    if new_student is None:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student with this email already exists"
        )

    return new_student


# ------------------------------------------------
# GET ALL STUDENTS
# ------------------------------------------------

@app.get(
    "/students",
    response_model=List[StudentResponse],
    status_code=status.HTTP_200_OK
)
def get_all_students(
    db: Session = Depends(get_db)
):

    return get_students(db)


# ------------------------------------------------
# GET STUDENT BY ID
# ------------------------------------------------

@app.get(
    "/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = get_student(
        db,
        student_id
    )

    if student is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# ------------------------------------------------
# UPDATE STUDENT
# ------------------------------------------------

@app.put(
    "/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def update_student_api(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    updated_student = update_student(
        db,
        student_id,
        student
    )

    if updated_student is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return updated_student


# ------------------------------------------------
# DELETE STUDENT
# ------------------------------------------------

@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student_api(
    student_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_student(
        db,
        student_id
    )

    if not deleted:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return None