from datetime import date

from pydantic import BaseModel

import models


class NameBaseModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class FacultyRead(NameBaseModel):
    pass


class DepartmentRead(NameBaseModel):
    pass


class YearRead(BaseModel):
    id: int
    start_year: int
    finish_year: int

    class Config:
        orm_mode = True


class SemesterRead(BaseModel):
    id: int
    number: int
    year: YearRead

    class Config:
        orm_mode = True


class GroupRead(NameBaseModel):
    faculty: FacultyRead
    department: DepartmentRead


class PersonBase(BaseModel):
    full_name: str
    date_of_birth: date

    class Config:
        orm_mode = True


class StudentCreate(PersonBase):
    group_id: int


class StudentReadShort(PersonBase):
    id: int


class StudentRead(StudentReadShort):
    group: GroupRead


class TeacherReadShort(PersonBase):
    id: int


class TeacherRead(TeacherReadShort):
    faculty: FacultyRead


class CourseProgramBase(BaseModel):
    theme: str
    academic_hours: int


class CourseProgramCreate(CourseProgramBase):
    pass

    class Meta:
        orm_model = models.CourseProgram


class CourseProgramRead(CourseProgramBase):
    id: int

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    course_programs: list[CourseProgramCreate] | None = []


class CourseReadShort(CourseBase):
    id: int


class CourseRead(CourseReadShort):
    course_programs: list[CourseProgramRead]


class GradeRead(BaseModel):
    id: int
    description: str
    value: int

    class Config:
        orm_mode = True


class EducationalPlanBase(BaseModel):
    id: int
    semester: SemesterRead
    course: CourseReadShort
    group: GroupRead

    class Config:
        orm_mode = True


class EducationalPlanRead(EducationalPlanBase):
    pass


class ExamBase(BaseModel):

    class Config:
        orm_mode = True


class ExamCreate(ExamBase):
    edu_plan_id: int
    examiner_id: int
    student_id: int
    grade_id: int
    protection_date: date


class ExamRead(ExamBase):
    id: int
    edu_plan: EducationalPlanRead
    examiner: TeacherReadShort
    student: StudentReadShort
    grade: GradeRead
    protection_date: date


class ExamUpdateGrade(BaseModel):
    grade_id: int
