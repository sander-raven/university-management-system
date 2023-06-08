from sqlalchemy import Column, Integer, String, ForeignKey, Date, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String(length=255), unique=True, nullable=False)
    info = Column(String(length=255))

    audiences = relationship("Audience", back_populates="building")


class Audience(Base):
    __tablename__ = "audiences"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(String(length=10), nullable=False)
    building_id = Column(Integer, ForeignKey("buildings.id"))

    building = relationship("Building", back_populates="audiences")
    schedules = relationship("Schedule", back_populates="audience")


class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=100), unique=True, nullable=False)

    groups = relationship("Group", back_populates="faculty")
    teachers = relationship("Teacher", back_populates="faculty")


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=20), unique=True, nullable=False)

    groups = relationship("Group", back_populates="department")


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=100), unique=True, nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculties.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))

    faculty = relationship("Faculty", back_populates="groups")
    department = relationship("Department", back_populates="groups")
    students = relationship("Student", back_populates="group")
    educational_plans = relationship("EducationalPlan", back_populates="group")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(length=255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))

    group = relationship("Group", back_populates="students")
    exams = relationship("Exam", back_populates="student")
    works = relationship("SelfstudyWork", back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(length=255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculties.id"))

    faculty = relationship("Faculty", back_populates="teachers")
    schedules = relationship("Schedule", back_populates="teacher")
    exams = relationship("Exam", back_populates="examiner")
    examiner_works = relationship(
        "SelfstudyWork",
        back_populates="examiner",
        foreign_keys="SelfstudyWork.examiner_id",
    )
    sci_adviser_works = relationship(
        "SelfstudyWork",
        back_populates="scientific_adviser",
        foreign_keys="SelfstudyWork.scientific_adviser_id",
    )


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(length=20), nullable=False)
    value = Column(Integer, nullable=False)

    exams = relationship("Exam", back_populates="grade")
    works = relationship("SelfstudyWork", back_populates="grade")


class Year(Base):
    __tablename__ = "years"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    start_year = Column(Integer, nullable=False)
    finish_year = Column(Integer, nullable=False)

    semesters = relationship("Semester", back_populates="year")


class Semester(Base):
    __tablename__ = "semesters"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    year_id = Column(Integer, ForeignKey("years.id"))

    educational_plans = relationship("EducationalPlan", back_populates="semester")
    year = relationship("Year", back_populates="semesters")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=100), unique=True, nullable=False)

    course_programs = relationship("CourseProgram", back_populates="course")
    educational_plans = relationship("EducationalPlan", back_populates="course")


class CourseProgram(Base):
    __tablename__ = "course_programs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    theme = Column(String(length=255), nullable=False)
    academic_hours = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"))

    course = relationship("Course", back_populates="course_programs")


class EducationalPlan(Base):
    __tablename__ = "educational_plans"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    semester_id = Column(Integer, ForeignKey("semesters.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))

    semester = relationship("Semester", back_populates="educational_plans")
    course = relationship("Course", back_populates="educational_plans")
    group = relationship("Group", back_populates="educational_plans")
    schedules = relationship("Schedule", back_populates="edu_plan")
    exams = relationship("Exam", back_populates="edu_plan")
    works = relationship("SelfstudyWork", back_populates="edu_plan")


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    edu_plan_id = Column(Integer, ForeignKey("educational_plans.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    audience_id = Column(Integer, ForeignKey("audiences.id"))
    start_at = Column(TIMESTAMP, nullable=False)

    edu_plan = relationship("EducationalPlan", back_populates="schedules")
    teacher = relationship("Teacher", back_populates="schedules")
    audience = relationship("Audience", back_populates="schedules")


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    edu_plan_id = Column(Integer, ForeignKey("educational_plans.id"))
    examiner_id = Column(Integer, ForeignKey("teachers.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    grade_id = Column(Integer, ForeignKey("grades.id"))
    protection_date = Column(Date, nullable=False)

    edu_plan = relationship("EducationalPlan", back_populates="exams")
    examiner = relationship("Teacher", back_populates="exams")
    student = relationship("Student", back_populates="exams")
    grade = relationship("Grade", back_populates="exams")


class SelfstudyWork(Base):
    __tablename__ = "selfstudy_works"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    edu_plan_id = Column(Integer, ForeignKey("educational_plans.id"))
    examiner_id = Column(Integer, ForeignKey("teachers.id"))
    scientific_adviser_id = Column(Integer, ForeignKey("teachers.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    grade_id = Column(Integer, ForeignKey("grades.id"))
    protection_date = Column(Date, nullable=False)

    edu_plan = relationship("EducationalPlan", back_populates="works")
    examiner = relationship(
        "Teacher",
        back_populates="examiner_works",
        foreign_keys="SelfstudyWork.examiner_id",
    )
    scientific_adviser = relationship(
        "Teacher",
        back_populates="sci_adviser_works",
        foreign_keys="SelfstudyWork.scientific_adviser_id",
    )
    student = relationship("Student", back_populates="works")
    grade = relationship("Grade", back_populates="works")
