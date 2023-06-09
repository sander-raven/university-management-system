# Описание API

Описание эндпоинтов.

Автоматически сгенерированная страница документации с их перечнем: http://127.0.0.1:8000/docs


## Содержание
1. [Создать студента](#создать-студента)
2. [Получить информацию о студенте по его id](#получить-информацию-о-студенте-по-его-id)
3. [Обновить информацию о студенте по его id](#обновить-информацию-о-студенте-по-его-id)
4. [Удалить студента по его id](#удалить-студента-по-его-id)
5. [Получить список всех преподавателей](#получить-список-всех-преподавателей)
6. [Создать новый курс](#создать-новый-курс)
7. [Получить информацию о курсе по его id](#получить-информацию-о-курсе-по-его-id)
8. [Получить список всех студентов на курсе](#получить-список-всех-студентов-на-курсе)
9. [Создать новую оценку для студента по курсу](#создать-новую-оценку-для-студента-по-курсу)
10. [Обновить оценку студента по курсу](#обновить-оценку-студента-по-курсу)


## Эндпоинты

### Создать студента

```http request
POST /students/
```

Параметры запроса:
- `full_name`: str, полное имя студента
- `date_of_birth`: str, дата рождения
- `group_id`: int, id группы студента

Пример запроса:
```json
{
  "full_name": "Филимонов Пётр Анатольевич",
  "date_of_birth": "1999-08-17",
  "group_id": 1
}
```

Параметры ответа:
- `full_name`: str, полное имя студента
- `date_of_birth`: str, дата рождения
- `id`: int, id студента
- `group`: вложенный json с объектом связанной группы
  - `id`: int, id группы
  - `name`: str, название группы

Пример ответа:
```json
{
  "full_name": "Филимонов Пётр Анатольевич",
  "date_of_birth": "1999-08-17",
  "id": 12,
  "group": {
    "id": 1,
    "name": "МАТ-01",
    "faculty": {
      "id": 1,
      "name": "Физико-математический"
    },
    "department": {
      "id": 1,
      "name": "очная"
    }
  }
}
```


### Получить информацию о студенте по его id

```http request
GET /students/{student_id}
```

Параметры запроса:
- `student_id`: int, id студента

Пример запроса:
```http request
GET /students/1
```

Параметры ответа:
- `full_name`: str, полное имя студента
- `date_of_birth`: str, дата рождения
- `id`: int, id студента
- `group`: вложенный json с объектом связанной группы
  - `id`: int, id группы
  - `name`: str, название группы

Пример ответа:
```json
{
  "full_name": "Иванов Иван Иванович",
  "date_of_birth": "1998-01-01",
  "id": 1,
  "group": {
    "id": 1,
    "name": "МАТ-01",
    "faculty": {
      "id": 1,
      "name": "Физико-математический"
    },
    "department": {
      "id": 1,
      "name": "очная"
    }
  }
}
```


### Обновить информацию о студенте по его id

```http request
PUT /students/{student_id}
```

Параметры запроса:
- `student_id`: int, id студента
- `full_name`: str, полное имя студента
- `date_of_birth`: str, дата рождения
- `group_id`: int, id группы студента

Пример запроса:
```http request
PUT /students/1
```
```json
{
  "full_name": "Иванов Иван Иванович",
  "date_of_birth": "1998-01-11",
  "group_id": 2
}
```

Параметры ответа:
- `full_name`: str, полное имя студента
- `date_of_birth`: str, дата рождения
- `id`: int, id студента
- `group`: вложенный json с объектом связанной группы
  - `id`: int, id группы
  - `name`: str, название группы

Пример ответа:
```json
{
  "full_name": "Иванов Иван Иванович",
  "date_of_birth": "1998-01-11",
  "id": 1,
  "group": {
    "id": 2,
    "name": "ФИЛ-02",
    "faculty": {
      "id": 2,
      "name": "Филологический"
    },
    "department": {
      "id": 1,
      "name": "очная"
    }
  }
}
```


### Удалить студента по его id

```http request
DELETE /students/{student_id}
```

Параметры запроса:
- `student_id`: int, id студента

Пример запроса:
```http request
DELETE /students/12
```

Пример ответа:

HTTP response status code - 204 No Content


### Получить список всех преподавателей

*Добавлена пагинация*

```http request
GET /students/{student_id}
```

Параметры запроса:
- `page`: int, номер страницы
- `size`: int, размер страницы

Пример запроса:
```http request
GET /teachers/?page=1&size=50
```

Параметры ответа:
- `items`: list, список преподавателей
  - `full_name`: str, полное имя преподавателя
  - `date_of_birth`: str, дата рождения
  - `id`: int, id преподавателя
  - `faculty`: вложенный json с объектом связанного факультета
    - `id`: int, id факультета
    - `name`: str, название факультета
- `total`: int, всего преподавателей
- `page`: int, номер страницы
- `size`: int, размер страницы
- `pages`: int, количество страниц

Пример ответа:
```json
{
  "items": [
    {
      "full_name": "Смирнов Александр Владимирович",
      "date_of_birth": "1980-01-01",
      "id": 1,
      "faculty": {
        "id": 2,
        "name": "Филологический"
      }
    },
    {
      "full_name": "Иванова Марина Сергеевна",
      "date_of_birth": "1975-02-02",
      "id": 2,
      "faculty": {
        "id": 1,
        "name": "Физико-математический"
      }
    },
    {
      "full_name": "Кузнецова Елена Ивановна",
      "date_of_birth": "1985-03-03",
      "id": 3,
      "faculty": {
        "id": 3,
        "name": "Иностранных языков"
      }
    },
    {
      "full_name": "Петров Михаил Викторович",
      "date_of_birth": "1990-04-04",
      "id": 4,
      "faculty": {
        "id": 1,
        "name": "Физико-математический"
      }
    },
    {
      "full_name": "Николаева Ольга Николаевна",
      "date_of_birth": "1995-05-05",
      "id": 5,
      "faculty": {
        "id": 2,
        "name": "Филологический"
      }
    }
  ],
  "total": 5,
  "page": 1,
  "size": 50,
  "pages": 1
}
```


### Создать новый курс

```http request
POST /courses
```

Параметры запроса:
- `name`: str, название курса
- `course_programs`: list, программа курса (опционально)
  - `theme`: str, тема
  - `academic_hours`: int, кол-во академических часов

Пример запроса:
```json
{
  "name": "Программирование",
  "course_programs": [
    {
      "theme": "Python",
      "academic_hours": 50
    },
    {
      "theme": "Алгоритмы",
      "academic_hours": 70
    }
  ]
}
```

Параметры ответа:
- `name`: str, название курса
- `id`: int, id курса
- `course_programs`: list, программа курса (опционально)
  - `theme`: str, тема
  - `academic_hours`: int, кол-во академических часов
  - `id`: int, id темы

Пример ответа:
```json
{
  "name": "Программирование",
  "id": 6,
  "course_programs": [
    {
      "theme": "Python",
      "academic_hours": 50,
      "id": 11
    },
    {
      "theme": "Алгоритмы",
      "academic_hours": 70,
      "id": 12
    }
  ]
}
```


### Получить информацию о курсе по его id

```http request
GET /courses/{course_id}
```

Параметры запроса:
- `course_id`: int, id курса

Пример запроса:
```http request
GET /courses/1
```

Параметры ответа:
- `name`: str, название курса
- `id`: int, id курса
- `course_programs`: list, программа курса (опционально)
  - `theme`: str, тема
  - `academic_hours`: int, кол-во академических часов
  - `id`: int, id темы

Пример ответа:
```json
{
  "name": "Математика",
  "id": 1,
  "course_programs": [
    {
      "theme": "Алгебра",
      "academic_hours": 60,
      "id": 1
    },
    {
      "theme": "Геометрия",
      "academic_hours": 50,
      "id": 2
    },
    {
      "theme": "Теория вероятностей",
      "academic_hours": 40,
      "id": 3
    }
  ]
}
```


### Получить список всех студентов на курсе

*Добавлена пагинация*

```http request
GET /courses/{course_id}/students
```

Параметры запроса:
- `course_id`: int, id курса
- `page`: int, номер страницы
- `size`: int, размер страницы

Пример запроса:
```http request
GET /courses/3/students?page=1&size=50
```

Параметры ответа:
- `items`: list, список студентов
  - `full_name`: str, полное имя студента
  - `date_of_birth`: str, дата рождения
  - `id`: int, id преподавателя
  - `group`: вложенный json с объектом связанной группы
    - `id`: int, id факультета
    - `name`: str, название факультета
    - `faculty`: вложенный json с объектом связанного факультета
    - `department`: вложенный json с объектом связанного отделения
- `total`: int, всего студентов
- `page`: int, номер страницы
- `size`: int, размер страницы
- `pages`: int, количество страниц

Пример ответа:
```json
{
  "items": [
    {
      "full_name": "Николаев Николай Николаевич",
      "date_of_birth": "1996-05-05",
      "id": 5,
      "group": {
        "id": 3,
        "name": "АНГ-03",
        "faculty": {
          "id": 3,
          "name": "Иностранных языков"
        },
        "department": {
          "id": 3,
          "name": "вечерняя"
        }
      }
    },
    {
      "full_name": "Петрова Анна Ивановна",
      "date_of_birth": "1998-06-06",
      "id": 6,
      "group": {
        "id": 3,
        "name": "АНГ-03",
        "faculty": {
          "id": 3,
          "name": "Иностранных языков"
        },
        "department": {
          "id": 3,
          "name": "вечерняя"
        }
      }
    },
    {
      "full_name": "Николаева Ольга Васильевна",
      "date_of_birth": "1997-09-09",
      "id": 9,
      "group": {
        "id": 3,
        "name": "АНГ-03",
        "faculty": {
          "id": 3,
          "name": "Иностранных языков"
        },
        "department": {
          "id": 3,
          "name": "вечерняя"
        }
      }
    }
  ],
  "total": 3,
  "page": 1,
  "size": 50,
  "pages": 1
}
```


### Создать новую оценку для студента по курсу

*В моей системе - это создание записи об экзамене*

```http request
POST /grades/
```

Параметры запроса:
- `edu_plan_id`: int, id плана обучения
- `examiner_id`: int, id экзаменатора
- `student_id`: int, id студента
- `grade_id`: int, id оценки
- `protection_date`: str, дата экзамена 

Пример запроса:
```json
{
  "edu_plan_id": 3,
  "examiner_id": 5,
  "student_id": 6,
  "grade_id": 1,
  "protection_date": "2021-12-24"
}
```

Параметры ответа:
- `id`: int, id экзамена
- `edu_plan`: объект связанного плана обучения
  - `semester`: объект семестра
    - ...
  - `course`: объект курса
    - ...
  - `group`: объект группы
    - ...
  - `id`: id плана обучения
- `examiner`: объект экзаменатора
  - `id`: int, id студента
  - `full_name`: str, полное имя
  - `date_of_birth`: int, дата рождения
- `student`: объект студента
  - `id`: int, id студента
  - `full_name`: str, полное имя
  - `date_of_birth`: int, дата рождения
- `grade`: объект оценки
  - `id`: int, id оценки
  - `description`: str, описание
  - `value`: int, значение
- `protection_date`: str, дата экзамена 

Пример ответа:
```json
{
  "id": 6,
  "edu_plan": {
    "id": 3,
    "semester": {
      "id": 1,
      "number": 1,
      "year": {
        "id": 1,
        "start_year": 2021,
        "finish_year": 2022
      }
    },
    "course": {
      "name": "Английский язык",
      "id": 3
    },
    "group": {
      "id": 3,
      "name": "АНГ-03",
      "faculty": {
        "id": 3,
        "name": "Иностранных языков"
      },
      "department": {
        "id": 3,
        "name": "вечерняя"
      }
    }
  },
  "examiner": {
    "full_name": "Николаева Ольга Николаевна",
    "date_of_birth": "1995-05-05",
    "id": 5
  },
  "student": {
    "full_name": "Петрова Анна Ивановна",
    "date_of_birth": "1998-06-06",
    "id": 6
  },
  "grade": {
    "id": 1,
    "description": "Отлично",
    "value": 5
  },
  "protection_date": "2021-12-24"
}
```


### Обновить оценку студента по курсу

*Изменение оценки экзамена*

```http request
PUT /grades/{grade_id}
```

Параметры запроса:
- `grade_id`: int, id экзамена (*Это path-параметр! Оставил таким же, как в задании.*)
- `grade_id`: int, id оценки (*Это параметр в теле запроса! Внешний ключ на справочник оценок*)

Пример запроса:
```http request
PUT /grades/6
```
```json
{
  "grade_id": 2
}
```

Параметры ответа:
- `id`: int, id экзамена
- `edu_plan`: объект связанного плана обучения
  - `semester`: объект семестра
    - ...
  - `course`: объект курса
    - ...
  - `group`: объект группы
    - ...
  - `id`: id плана обучения
- `examiner`: объект экзаменатора
  - `id`: int, id студента
  - `full_name`: str, полное имя
  - `date_of_birth`: int, дата рождения
- `student`: объект студента
  - `id`: int, id студента
  - `full_name`: str, полное имя
  - `date_of_birth`: int, дата рождения
- `grade`: объект оценки
  - `id`: int, id оценки
  - `description`: str, описание
  - `value`: int, значение
- `protection_date`: str, дата экзамена 

Пример ответа:
```json
{
  "id": 6,
  "edu_plan": {
    "id": 3,
    "semester": {
      "id": 1,
      "number": 1,
      "year": {
        "id": 1,
        "start_year": 2021,
        "finish_year": 2022
      }
    },
    "course": {
      "name": "Английский язык",
      "id": 3
    },
    "group": {
      "id": 3,
      "name": "АНГ-03",
      "faculty": {
        "id": 3,
        "name": "Иностранных языков"
      },
      "department": {
        "id": 3,
        "name": "вечерняя"
      }
    }
  },
  "examiner": {
    "full_name": "Николаева Ольга Николаевна",
    "date_of_birth": "1995-05-05",
    "id": 5
  },
  "student": {
    "full_name": "Петрова Анна Ивановна",
    "date_of_birth": "1998-06-06",
    "id": 6
  },
  "grade": {
    "id": 2,
    "description": "Хорошо",
    "value": 4
  },
  "protection_date": "2021-12-24"
}
```
