-- buildings
CREATE TABLE IF NOT EXISTS buildings (
	id SERIAL PRIMARY KEY,
	address VARCHAR(255) UNIQUE NOT NULL,
	info VARCHAR(255) NULL
);

-- audiences
CREATE TABLE IF NOT EXISTS audiences (
	id SERIAL PRIMARY KEY,
	number VARCHAR(10) NOT NULL,
	building_id INT NOT NULL,
	FOREIGN KEY (building_id) REFERENCES buildings (id),
	UNIQUE (number, building_id)
);

-- faculties
CREATE TABLE IF NOT EXISTS faculties (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) UNIQUE NOT NULL
);

-- departments
CREATE TABLE IF NOT EXISTS departments (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) UNIQUE NOT NULL
);

-- groups
CREATE TABLE IF NOT EXISTS groups (
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) UNIQUE NOT NULL,
	faculty_id INT NOT NULL,
	department_id INT NOT NULL,
	FOREIGN KEY (faculty_id) REFERENCES faculties (id),
	FOREIGN KEY (department_id) REFERENCES departments (id)
);

-- students
CREATE TABLE IF NOT EXISTS students (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(255) NOT NULL,
	date_of_birth DATE NOT NULL,
	group_id INT NOT NULL,
	FOREIGN KEY (group_id) REFERENCES groups (id)
);

-- teachers
CREATE TABLE IF NOT EXISTS teachers (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(255) NOT NULL,
	date_of_birth DATE NOT NULL,
	faculty_id INT NOT NULL,
	FOREIGN KEY (faculty_id) REFERENCES faculties (id)
);

-- grades
CREATE TABLE IF NOT EXISTS grades (
	id SERIAL PRIMARY KEY,
	description VARCHAR(20) NOT NULL,
	value INT NOT NULL,
	UNIQUE (description, value)
);

-- years
CREATE TABLE IF NOT EXISTS years (
	id SERIAL PRIMARY KEY,
	start_year INT NOT NULL,
	finish_year INT NOT NULL,
	UNIQUE(start_year, finish_year)
);

-- semesters
CREATE TABLE IF NOT EXISTS semesters (
	id SERIAL PRIMARY KEY,
	number INT NOT NULL,
	year_id INT NOT NULL,
	FOREIGN KEY (year_id) REFERENCES years (id),
	UNIQUE (number, year_id)
);

-- courses
CREATE TABLE IF NOT EXISTS courses (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) UNIQUE NOT NULL
);

-- course_programs
CREATE TABLE IF NOT EXISTS course_programs (
	id SERIAL PRIMARY KEY,
	theme VARCHAR(255) NOT NULL,
	academic_hours INT NOT NULL,
	course_id INT NOT NULL,
	FOREIGN KEY (course_id) REFERENCES courses (id),
	UNIQUE (theme, course_id)
);

-- educational_plans
CREATE TABLE IF NOT EXISTS educational_plans (
	id SERIAL PRIMARY KEY,
	semester_id INT NOT NULL,
	course_id INT NOT NULL,
	group_id INT NOT NULL,
	FOREIGN KEY (semester_id) REFERENCES semesters (id),
	FOREIGN KEY (course_id) REFERENCES courses (id),
	FOREIGN KEY (group_id) REFERENCES groups (id),
	UNIQUE (semester_id, course_id, group_id)
);

-- schedules
CREATE TABLE IF NOT EXISTS schedules (
	id SERIAL PRIMARY KEY,
	edu_plan_id INT NOT NULL,
	teacher_id INT NOT NULL,
	audience_id INT NOT NULL,
	start_at timestamp NOT NULL,
	FOREIGN KEY (edu_plan_id) REFERENCES educational_plans (id),
	FOREIGN KEY (teacher_id) REFERENCES teachers (id),
	FOREIGN KEY (audience_id) REFERENCES audiences (id),
	UNIQUE (teacher_id, start_at),
	UNIQUE (audience_id, start_at)
);

-- exams
CREATE TABLE IF NOT EXISTS exams (
	id SERIAL PRIMARY KEY,
	edu_plan_id INT NOT NULL,
	examiner_id INT NOT NULL,
	student_id INT NOT NULL,
	grade_id INT NOT NULL,
	protection_date DATE NOT NULL,
	FOREIGN KEY (edu_plan_id) REFERENCES educational_plans (id),
	FOREIGN KEY (examiner_id) REFERENCES teachers (id),
	FOREIGN KEY (student_id) REFERENCES students (id),
	FOREIGN KEY (grade_id) REFERENCES grades (id)
);

-- selfstudy_works
CREATE TABLE IF NOT EXISTS selfstudy_works (
	id SERIAL PRIMARY KEY,
	edu_plan_id INT NOT NULL,
	examiner_id INT NOT NULL,
	scientific_adviser_id INT NOT NULL,
	student_id INT NOT NULL,
	grade_id INT NOT NULL,
	protection_date DATE NOT NULL,
	theme VARCHAR(255) UNIQUE NOT NULL,
	FOREIGN KEY (edu_plan_id) REFERENCES educational_plans (id),
	FOREIGN KEY (examiner_id) REFERENCES teachers (id),
	FOREIGN KEY (scientific_adviser_id) REFERENCES teachers (id),
	FOREIGN KEY (student_id) REFERENCES students (id),
	FOREIGN KEY (grade_id) REFERENCES grades (id)
);
