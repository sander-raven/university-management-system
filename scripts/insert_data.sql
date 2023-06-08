-- buildings
INSERT INTO buildings (address, info)
VALUES
	('ул. Ленина, д. 24, к. 1', 'Главный корпус'),
	('ул. Ленина, д. 26', NULL),
	('ул. Пушкина, д. 17', 'Здание №3');

-- audiences
INSERT INTO audiences (number, building_id)
VALUES
	('101', 1),
	('102', 1),
	('203', 1),
	('15а', 2),
	('1А', 3),
	('27', 3);

-- faculties
INSERT INTO faculties (name)
VALUES
	('Физико-математический'),
	('Филологический'),
	('Иностранных языков');

-- departments
INSERT INTO departments (name)
VALUES
	('очная'),
	('заочная'),
	('вечерняя');

-- groups
INSERT INTO groups (name, faculty_id, department_id)
VALUES
	('МАТ-01', 1, 1),
	('ФИЛ-02', 2, 1),
	('АНГ-03', 3, 3);

-- students
INSERT INTO students (full_name, date_of_birth, group_id)
VALUES
	('Иванов Иван Иванович', '1998-01-01', 1),
	('Петров Петр Петрович', '1999-02-02', 1),
	('Сидоров Сидор Сидорович', '2000-03-03', 2),
	('Кузнецов Кузьма Кузьмич', '1997-04-04', 2),
	('Николаев Николай Николаевич', '1996-05-05', 3),
	('Петрова Анна Ивановна', '1998-06-06', 3),
	('Сидорова Елена Сергеевна', '1999-07-07', 1),
	('Кузнецова Мария Владимировна', '2000-08-08', 2),
	('Николаева Ольга Васильевна', '1997-09-09', 3),
	('Иванова Татьяна Петровна', '1996-10-10', 1);

-- teachers
INSERT INTO teachers (full_name, date_of_birth, faculty_id)
VALUES
	('Смирнов Александр Владимирович', '1980-01-01', 2),
	('Иванова Марина Сергеевна', '1975-02-02', 1),
	('Кузнецова Елена Ивановна', '1985-03-03', 3),
	('Петров Михаил Викторович', '1990-04-04', 1),
	('Николаева Ольга Николаевна', '1995-05-05', 2);

-- grades
INSERT INTO grades (description, value)
VALUES
	('Отлично', 5),
	('Хорошо', 4),
	('Удовлетворительно', 3),
	('Неудовлетворительно', 2);

-- years
INSERT INTO years (start_year, finish_year)
VALUES
	(2021, 2022),
	(2022, 2023);

-- semesters
INSERT INTO semesters (number, year_id)
VALUES
	(1, 1),
	(2, 1),
	(1, 2);

-- courses
INSERT INTO courses (name)
VALUES
	('Математика'),
	('Русский язык'),
	('Английский язык');

-- course_programs
INSERT INTO course_programs (theme, academic_hours, course_id)
VALUES
	('Алгебра', 60, 1),
	('Геометрия', 50, 1),
	('Теория вероятностей', 40, 1),
	('Грамматика', 70, 2),
	('Синтаксис', 50, 2),
	('Стилистика', 40, 2),
	('Грамматика', 60, 3),
	('Лексика', 50, 3),
	('Аудирование', 40, 3);

-- educational_plans
INSERT INTO educational_plans (semester_id, course_id, group_id)
VALUES
	(2, 1, 1),
	(2, 2, 2),
	(1, 3, 3);

-- schedules
INSERT INTO schedules (edu_plan_id, teacher_id, audience_id, start_at)
VALUES
	(1, 1, 1, '2021-09-02 09:00:00'),
	(2, 3, 4, '2021-09-02 09:00:00'),
	(3, 5, 5, '2021-09-02 09:00:00'),
	(1, 1, 1, '2021-09-03 09:00:00'),
	(2, 3, 4, '2021-09-03 09:00:00'),
	(3, 5, 5, '2021-09-03 09:00:00'),
	(1, 1, 2, '2021-09-04 09:00:00'),
	(1, 2, 2, '2021-09-04 10:00:00'),
	(2, 4, 4, '2021-09-04 09:00:00'),
	(3, 5, 5, '2021-09-04 09:00:00'),
	(1, 2, 6, '2021-09-05 10:00:00'),
	(2, 3, 3, '2021-09-05 09:00:00'),
	(3, 5, 1, '2021-09-05 09:00:00'),
	(2, 4, 1, '2021-09-05 10:00:00');

-- exams
INSERT INTO exams (edu_plan_id, examiner_id, student_id, grade_id, protection_date)
VALUES
	(1, 1, 1, 1, '2021-12-24'),
	(1, 1, 2, 2, '2021-12-24'),
	(1, 1, 7, 1, '2021-12-24'),
	(1, 1, 10, 3, '2021-12-24');

-- selfstudy_works
INSERT INTO selfstudy_works (edu_plan_id, examiner_id, scientific_adviser_id, student_id, grade_id, protection_date, theme)
VALUES
	(2, 3, 4, 3, 2, '2021-12-20', 'Тема курсовой 1'),
	(2, 4, 3, 4, 1, '2022-12-20', 'Тема курсовой 2');
