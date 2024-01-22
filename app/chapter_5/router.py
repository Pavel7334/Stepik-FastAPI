from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["Chapter_5:"]
)

#                                                       5.1

#                                        Понимание интеграции баз данных

"""Интеграция баз данных является важнейшим аспектом веб-приложений, поскольку она позволяет эффективно хранить, 
извлекать данные и управлять ими. FastAPI обеспечивает надежную поддержку интеграции различных баз данных в ваше 
приложение, позволяя вам беспрепятственно работать со структурированными данными. В этом уроке мы рассмотрим, как 
подключить FastAPI к базам данных и выполнять основные операции с базами данных."""

#                                       Поддерживаемые базы данных в FastAPI

"""FastAPI поддерживает широкий спектр баз данных, включая:

SQLite: Облегченная бессерверная база данных, которая хранит данные в локальном файле.
PostgreSQL: Мощная система управления реляционными базами данных с открытым исходным кодом, известная своей 
производительностью и масштабируемостью. 
MySQL: Популярная система реляционных баз данных, которая известна своей надёжностью.
MongoDB: База данных NoSQL (нереляционная), которая хранит данные в гибких документах, подобных JSON."""

#                                          Подключение FastAPI к базе данных

"""Чтобы подключить FastAPI к базе данных, вам необходимо выполнить следующие общие действия:

Шаг 1: Установите драйвер базы данных. Сначала установите соответствующий драйвер базы данных для выбранной вами базы 
данных. Например, если вы планируете использовать PostgreSQL, установите библиотеку `asyncpg` для асинхронного доступа 
или `psycopg2` для синхронного доступа. 
Шаг 2: Импортируйте драйвер базы данных. В вашем приложении FastAPI импортируйте необходимый модуль драйвера базы 
данных.
Шаг 3: Настройте подключение к базе данных. Настройте параметры подключения к базе данных, такие как URL-адрес базы 
данных, имя пользователя, пароль и другие соответствующие конфигурации.
Шаг 4: Создайте сеанс работы с базой данных. Создайте сеанс базы данных или пул подключений, который ваше приложение 
FastAPI может использовать для взаимодействия с базой данных."""

#                                           Выполнение операций CRUD

"""Как только ваше приложение FastAPI подключено к базе данных, вы можете выполнять операции CRUD 
(создавать, читать, обновлять, удалять) с вашими данными.

Создать (CREATE): Вставить новые записи данных в базу данных.
ЧИТАТЬ (READ): Извлекать данные из базы данных на основе определенных критериев.
ОБНОВИТЬ (UPDATE): Изменить существующие записи данных в базе данных.
УДАЛИТЬ (DELETE): Удалить записи данных из базы данных.
Более подробно данные операции будут рассмотрены в следующем уроке. """

#                                           Асинхронный доступ к базе данных

"""Встроенная поддержка асинхронного программирования в FastAPI позволяет вам использовать преимущества асинхронного 
доступа к базе данных. Используя синтаксис async/await с запросами к базе данных, ваше приложение может эффективно 
обрабатывать несколько запросов одновременно, что приводит к повышению производительности и масштабируемости.

Обратите внимание, что некоторые базы данных не позволяют асинхронно выполнять операции с целью поддержания 
стабильности данных. Поэтому существует мнение о "неэффективности" асинхронного программирования в Python 
(т.к. в конечном итоге приложение, которое может иметь сколько угодно потоков исполнения) все равно будет "ходить" 
в базу данных, которая все запросы будет обрабатывать по-очереди синхронно.

На следующем уроке мы углубимся в выполнение CRUD-операций и работу с базами данных в FastAPI.

Примечание: При работе с базами данных в производственных приложениях не забывайте применять надлежащие меры 
безопасности, эффективно обрабатывать подключения к базе данных и оптимизировать запросы для обеспечения наилучшей 
производительности."""

#                                       Задача на программирование повышенной сложности

# Для этой задачи программирования вам необходимо интегрировать FastAPI с базой данных и выполнить базовые операции
# CRUD с определенным ресурсом.
#
# Требования:
#
# 1. Выберите любую поддерживаемую базу данных (например, SQLite, PostgreSQL, MySQL или MongoDB) и установите
# необходимый драйвер базы данных для FastAPI (рекомендуется выбирать ту, с которой больше всего вероятность работать
# в будущем, либо ту, с которой вы ещё не умеете работать).
#
# 2. Создайте модель данных (схему) для простого ресурса (например, элемента "Todo" (воображаемый список дел),
#  который включает такие поля, как "id", "title" (заголовок), "description" (описание) и "completed" (завершено).
#
# 3. Реализуйте конечную точку FastAPI для создания нового элемента "Todo". Конечная точка должна принимать
#  POST-запросом полезную нагрузку JSON, содержащую поля "заголовок" и "описание". После успешного создания верните
#  созданный элемент "Todo" в ответе (по умолчанию у нового элемента статус (признак) завершено равен False).
#
# 4. Реализуйте конечную точку FastAPI для извлечения одного элемента "Todo" на основе его "id". Конечная точка на
#  GET-запрос должна возвращать соответствующий элемент "Todo", если он найден, или соответствующий ответ об ошибке,
#   если элемент не существует.
#
# 5. Реализуйте конечную точку FastAPI для обновления существующего элемента "Todo" на основе его "id". Конечная
#  точка должна принимать полезную нагрузку JSON (PUT/POST-запрос), содержащую поля "заголовок", "описание" и
#  "завершено". Обновите соответствующий элемент "Todo" в базе данных и верните обновленный элемент в ответе.
#
# 6. Реализуйте конечную точку FastAPI для удаления элемента "Todo" на основе его "id". Если элемент успешно удален,
#  верните сообщение об успешном завершении в ответе.
#
# Пример POST-запроса create (Создать Todo):
#
# POST /todos
# Content-Type: application/json
#
# {
#   "title": "Buy groceries",
#   "description": "Milk, eggs, bread"
# }
# Пример ответа (201 Created):
#
# {
#   "id": 1,
#   "title": "Buy groceries",
#   "description": "Milk, eggs, bread",
#   "completed": false
# }
# Пример GET-запроса read (Получить Todo - ID: 1):
#
# GET /todos/1
# Пример ответа (200 OK):
#
# {
#   "id": 1,
#   "title": "Buy groceries",
#   "description": "Milk, eggs, bread",
#   "completed": false
# }

#                                                   Решение 1

# main.py:
#
# from fastapi import FastAPI
# from router.router import router as router_db
#
# app = FastAPI()
#
# app.include_router(router_db)
# router.py:
#
# from fastapi import APIRouter
# from dao import ToDoDAO
#
# router = APIRouter(
#     prefix="/db",
#     tags=["To Do tasks"]
# )
#
#
# @router.get("/get_tasks")
# async def get(title: str):
#     return await ToDoDAO.get_tasks(title=title)
#
#
# @router.post("/add_task")
# async def add(title: str, description: str, completed: str):
#     await ToDoDAO.add_task(title=title, description=description, completed=completed)
#     return {"message": f"{title} was added!"}
#
#
# @router.put("/update_task")
# async def update(title: str, completed: str):
#     await ToDoDAO.update_task(title, completed)
#     return {"message": f"{title} was changed!"}
#
#
# @router.delete("/delete_task")
# async def delete(title: str):
#     await ToDoDAO.delete_task(title)
#     return {"message": f"{title} was deleted!"}
#
#
# database.py:
#
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker
# from config import settings
#
# engine = create_async_engine(settings.DATABASE_URL)
#
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# dao.py:
#
# from sqlalchemy import select, delete, insert, update
# from database import async_session_maker
# from models_sql import ToDo
#
#
# class ToDoDAO:
#     model = ToDo
#
#     @classmethod
#     async def get_tasks(cls, **filter_by):
#         async with async_session_maker() as session:
#             query = select("*").select_from(cls.model).filter_by(**filter_by)
#             result = await session.execute(query)
#             return result.mappings().all()
#
#     @classmethod
#     async def add_task(cls, **data):
#         async with async_session_maker() as session:
#             query = insert(cls.model).values(**data)
#             await session.execute(query)
#             await session.commit()
#
#     @classmethod
#     async def update_task(cls, title, completed):
#         async with async_session_maker() as session:
#             query = update(cls.model).where(cls.model.title == title).values(completed=completed)
#             await session.execute(query)
#             await session.commit()
#
#     @classmethod
#     async def delete_task(cls, title):
#         async with async_session_maker() as session:
#             query = delete(cls.model).where(cls.model.title == title)
#             await session.execute(query)
#             await session.commit()

#  РЕШЕНИЕ 2 на GITHUB https://github.com/KonstantinScheglov