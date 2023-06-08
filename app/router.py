from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import paginate, Page
from sqlalchemy.orm import Session

import schemas
import models
from database import get_db
from utils import parse_pydantic_schema

router = APIRouter(tags=["University"])


@router.post("/students/", response_model=schemas.StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.get("/students/{student_id}", response_model=schemas.StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Студент с id {student_id} не найден")


@router.put("/students/{student_id}", response_model=schemas.StudentRead)
def update_student(student_id: int, payload: schemas.StudentCreate, db: Session = Depends(get_db)):
    filtered = db.query(models.Student).filter(models.Student.id == student_id)
    student = filtered.first()
    if student:
        filtered.update(payload.dict(), synchronize_session=False)
        db.commit()
        db.refresh(student)
        return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Студент с id {student_id} не найден")


@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Студент с id {student_id} не найден",
        )
    db.delete(student)
    db.commit()


@router.get("/teachers/", response_model=Page[schemas.TeacherRead])
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(models.Teacher).all()
    return paginate(teachers)


@router.post("/courses/", response_model=schemas.CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    new_course = models.Course(**parse_pydantic_schema(course))
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@router.get("/courses/{course_id}", response_model=schemas.CourseRead)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course:
        return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Курс с id {course_id} не найден")


@router.get("/courses/{course_id}/students", response_model=Page[schemas.StudentRead])
def get_course_students(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course:
        students = db.query(models.Student).distinct()\
            .join(models.EducationalPlan, models.Student.group_id == models.EducationalPlan.group_id)\
            .where(models.EducationalPlan.course_id == course_id).all()
        return paginate(students)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Курс с id {course_id} не найден")


@router.get("/exam/{exam_id}", response_model=schemas.ExamRead)
def get_exam(exam_id: int, db: Session = Depends(get_db)):
    exam = db.query(models.Exam).filter(models.Exam.id == exam_id).first()
    if exam:
        return exam
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Экзамен с id {exam_id} не найден")


@router.post("/grades", response_model=schemas.ExamRead)
def create_exam(exam: schemas.ExamCreate, db: Session = Depends(get_db)):
    new_exam = models.Exam(**exam.dict())
    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)
    return new_exam


@router.put("/grades/{grade_id}", response_model=schemas.ExamRead)
def update_exam_grade(grade_id: int, payload: schemas.ExamUpdateGrade, db: Session = Depends(get_db)):
    filtered = db.query(models.Exam).filter(models.Exam.id == grade_id)
    exam = filtered.first()
    if exam:
        filtered.update(payload.dict(), synchronize_session=False)
        db.commit()
        db.refresh(exam)
        return exam
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Экзамен с id {grade_id} не найден")
