# University Management System

Реализация веб-сервиса "Система управления университетом" в рамках тестового задания.


## Тестовое задание

Текст задания – [**docs/Техническое_задание.md**](docs/Техническое_задание.md).


## Используемые технологии

**PostgreSQL** – СУБД.

**psycopg2-binary** – адаптер PostgreSQL для Python.

**FastAPI** – веб-фреймворк.

**fastapi-pagination** – библиотека для пагинации в FastAPI.

**SQLAlchemy** – ORM.

**pydantic** – библиотека для валидации данных.

**uvicorn** – веб-сервер.


## Описание структуры БД

...


## Описание структуры приложения FastAPI

Приложение находится в каталоге `app` и содержит следующие файлы:

`__init__.py` – пустой файл, указывающий, что `app` – пакет python.

`config.py` – конфигурация приложения.

`database.py` – настройка подключения к БД и сессии.

`main.py` – главный модуль приложения.

`models.py` – SQLAlchemy-модели сущностей БД.

`router.py` – эндпоинты API и обрабатывающие их функции.

`schemas.py` – Pydantic-модели сущностей БД.

`utils.py` – вспомогательные функции.

`Dockerfile` – описание контейнера приложения.

`entrypoint.sh` – bash-скрипт для ожидания старта PostgreSQL.

`requirements.txt` – перечень необходимых зависимостей.


## Предварительно

Для запуска приложения используются `Docker` и `Docker Compose`. Убедитесь, что они установлены в системе.


## Установка и запуск

Клонируйте репозиторий:
```shell
git clone git@github.com:sander-raven/university-management-system.git
```

Перейдите в главную директорию проекта:
```shell
cd university-management-system/
```

Переименуйте директорию `env-sample` в `env`:
```shell
mv env-sample/ env/
```

Задайте необходимые значения переменным в файлах `env/.env.app` и `env/.env.db`. Например:
```shell
nano env/.env.app
```

Запустите контейнеры:
```shell
docker compose up -d --build
```

Создайте таблицы БД. (В примере: имя пользователя – `university_user`, имя базы данных – `university`):
```shell
docker exec -i univer-db psql -U university_user -d university < ./scripts/create_tables.sql 
```

Заполните таблицы данными:
```shell
docker exec -i univer-db psql -U university_user -d university < ./scripts/insert_data.sql
```

**Перейдите в браузере по адресу http://127.0.0.1:8000/docs. Перед вами откроется страница с эндпоинтами API-сервиса Системы управления университетом.**

*Для остановки и удаления контейнеров используйте следующую команду (флаг `-v` также удалит том с базой данных):*
```shell
docker compose down -v
```


## Использование API

...


## Автор
Александр Аравин - [sander-raven](https://github.com/sander-raven). Email: sander-raven@yandex.ru.


## Лицензия
Проект находится под лицензией MIT. Подробнее: смотри файл [LICENSE](LICENSE).
