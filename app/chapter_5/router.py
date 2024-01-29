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


#                                                       5.2

#                                           Введение в операции CRUD

"""Операции CRUD (создание, чтение, обновление, удаление) - это фундаментальные операции, используемые в управлении 
базами данных для взаимодействия с данными, хранящимися в базе данных. В этом уроке мы углубимся в выполнение 
CRUD-операций с помощью FastAPI и рассмотрим, как манипулировать данными в подключенной базе данных.

Так как в FastAPI могут применяться различные базы данных, синтаксис которых может различаться, либо вы можете 
использовать более удобные формы взаимодействия с базами данных, такие как ORM (например PonyORM, peewee и др.), 
то примеры кода в данном уроке будут носить ознакомительный характер. Мы будем использовать PostgreSQL, так как в 
настоящее время это наиболее распространённая БД в российском продакшене (исходя из требований на hh.ru).

В связи с тем, что для разработки северной части приложения в большинстве случаев требуется умение работать с БД, 
настоятельно рекомендуем вам пройти курсы по этой тематике (на степике имеются как платные, так и бесплатные).

Например курс "Введение в базы данных" 

https://stepik.org/course/551/"""


#                                               Операция CREATE

# Операция "Создать" (create) включает в себя добавление новых записей или вводимых данных в базу данных. В FastAPI
# вы можете создать новую запись, обработав запрос (например, POST-запрос) с соответствующими данными и сохранив его
# в базе данных.
#
# Чтобы продемонстрировать операцию "CREATE" с использованием PostgreSQL в FastAPI, мы будем использовать библиотеку
# "databases" в качестве драйвера асинхронной базы данных и PostgreSQL в качестве базы данных.
#
# Шаг 1: Установите необходимые библиотеки
#
# Во-первых, убедитесь, что у вас установлены необходимые библиотеки. Вы можете установить FastAPI, Uvicorn
# (сервер ASGI), а также адаптер базы PostgreSQL, выполнив следующую команду:
#
# pip install fastapi uvicorn databases[asyncpg]
# Шаг 2: Создайте приложение FastAPI
#
# Создайте новый файл с именем `main.py` и добавьте следующий код:
#
# from fastapi import FastAPI, HTTPException
# from databases import Database
# from pydantic import BaseModel
# from typing import Optional
#
# app = FastAPI()
#
# # URL для PostgreSQL (измените его под свою БД)
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
#
# database = Database(DATABASE_URL)
#
#
# # Модель User для валидации входных данных
# class UserCreate(BaseModel):
#     username: str
#     email: str
#
#
# # Модель User для валидации исходящих данных - чисто для демонстрации (обычно входная модель шире чем выходная, т.к.
# на вход мы просим, например, пароль, который обратно не возвращаем, и другое, что не обязательно возвращать)
# class UserReturn(BaseModel):
#     username: str
#     email: str
#     id: Optional[int] = None
#
#
# # тут устанавливаем условия подключения к базе данных и отключения - можно использовать в роутах контекстный
# менеджер async with Database(...) as db: etc
# @app.on_event("startup")
# async def startup_database():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown_database():
#     await database.disconnect()
#
#
# # создание роута для создания юзеров
# @app.post("/users/", response_model=UserReturn)
# async def create_user(user: UserCreate):
#     query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
#     values = {"username": user.username, "email": user.email}
#     try:
#         user_id = await database.execute(query=query, values=values)
#         return {**user.dict(), "id": user_id}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create user")
# Шаг 3: Настройка базы данных PostgreSQL
#
# Убедитесь, что у вас запущен сервер PostgreSQL, и создайте новую базу данных и таблицу. Для этого примера давайте
# предположим, что у вас есть база данных с именем "mydatabase" и таблица с именем "users" со следующей структурой:
#
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL
# );
# Шаг 4: Запустите приложение
#
# Чтобы запустить приложение FastAPI, используйте следующую команду:
#
# uvicorn main:app --reload
# Шаг 5: Протестируйте операцию "CREATE"
#
# Используйте такой инструмент, как "httpie" или Postman, чтобы протестировать операцию "Создать", отправив
# POST-запрос с пользовательскими данными:
#
# На httpie:
#
# http POST http://localhost:8000/users/ username="john_doe" email="john.doe@example.com"
# Ответ должен быть таким:
#
# {
#     "username": "john_doe",
#     "email": "john.doe@example.com",
#     "id": 1
# }
# Пользователь был успешно добавлен в базу данных PostgreSQL с уникальным идентификатором.
#
# Теперь у вас есть приложение FastAPI, которое демонстрирует операцию "Создать" с использованием PostgreSQL.
# Не забудьте настроить URL-адрес подключения к базе данных и структуру таблицы в соответствии с вашими конкретными
# настройками базы данных PostgreSQL и учетными данными. Также можете использовать PGAdmin для создания и просмотра
# содержимого вашей PostgreSQL базы данных. Например, можно использовать SQL-запрос прямо в PGAdmin:
#
# SELECT * FROM users;


#                                               Операция READ

# Операция "Чтение" включает в себя извлечение данных из базы данных на основе определенных критериев, таких как
# идентификатор или параметры фильтрации. В FastAPI вы можете реализовать операции чтения, используя различные
# HTTP-методы, такие как запросы GET для извлечения данных из базы данных.
#
# Можно расширить предыдущий код, добавив в него следующее:
#
# from fastapi import FastAPI, HTTPException
# from databases import Database
# from pydantic import BaseModel
# from typing import Optional
#
# app = FastAPI()
#
# # URL для PostgreSQL (измените его под свою БД)
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
#
# database = Database(DATABASE_URL)
#
#
# # Модель User для валидации входных данных
# class UserCreate(BaseModel):
#     username: str
#     email: str
#
#
# # Модель User для валидации исходящих данных
# class UserReturn(BaseModel):
#     username: str
#     email: str
#     id: Optional[int] = None
#
#
# # тут устанавливаем условия подключения к базе данных и отключения
# @app.on_event("startup")
# async def startup_database():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown_database():
#     await database.disconnect()
#
#
# # создание роута для создания юзеров
# @app.post("/users/", response_model=UserReturn)
# async def create_user(user: UserCreate):
#     query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
#     values = {"username": user.username, "email": user.email}
#     try:
#         user_id = await database.execute(query=query, values=values)
#         return {**user.dict(), "id": user_id}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create user")
#
#
# # маршрут для получения информации о юзере по ID
# @app.get("/user/{user_id}", response_model=UserReturn)
# async def get_user(user_id: int):
#     query = "SELECT * FROM users WHERE id = :user_id"
#     values = {"user_id": user_id}
#     try:
#         result = await database.fetch_one(query=query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to fetch user from database")
#     if result:
#         return UserReturn(username=result["username"], email=result["email"])
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
#
# В приведенном выше коде мы добавили новый маршрут с именем `/user/{user_id}`, который принимает user_id в
# качестве параметра пути. Когда на этот маршрут отправляется запрос GET с действительным user_id, приложение
# запрашивает базу данных для пользователя с этим идентификатором и возвращает информацию пользователя в качестве
# ответа.
#
# Например, если вы создаете пользователя с запросом POST (пример без httpie):
#
# POST http://localhost:8000/users/
#
# {
#     "username": "vasya_pupkin",
#     "email": "super_puper_mega_man@example.com"
# }
# То ответ будет:
#
# {
#     "username": "vasya_pupkin",
#     "email": "super_puper_mega_man@example.com",
#     "id": 2
# }
# Попробуйте отправить такой запрос (или можете поэкспериментировать с несуществующими id):
#
# GET http://localhost:8000/user/1


#                                               Операция UPDATE

# Операция "Обновление" включает в себя изменение существующих записей или вводов данных в базе данных. В FastAPI вы
# можете обрабатывать операции обновления, получая запрос с обновленными данными и обновляя соответствующую запись в
# базе данных.
#
# Продолжаем заниматься модификацией нашего кода:
#
# from fastapi import FastAPI, HTTPException
# from databases import Database
# from pydantic import BaseModel
# from typing import Optional
#
# app = FastAPI()
#
# # URL для PostgreSQL (измените его под свою БД)
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
#
# database = Database(DATABASE_URL)
#
#
# # Модель User для валидации входных данных
# class UserCreate(BaseModel):
#     username: str
#     email: str
#
#
# # Модель User для валидации исходящих данных
# class UserReturn(BaseModel):
#     username: str
#     email: str
#     id: Optional[int] = None
#
#
# # тут устанавливаем условия подключения к базе данных и отключения
# @app.on_event("startup")
# async def startup_database():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown_database():
#     await database.disconnect()
#
#
# # создание роута для создания юзеров
# @app.post("/users/", response_model=UserReturn)
# async def create_user(user: UserCreate):
#     query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
#     values = {"username": user.username, "email": user.email}
#     try:
#         user_id = await database.execute(query=query, values=values)
#         return {**user.dict(), "id": user_id}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create user")
#
# # маршрут для получения информации о юзере по ID
# @app.get("/user/{user_id}", response_model=UserReturn)
# async def get_user(user_id: int):
#     query = "SELECT * FROM users WHERE id = :user_id"
#     values = {"user_id": user_id}
#     try:
#         result = await database.fetch_one(query=query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to fetch user from database")
#     if result:
#         return UserReturn(username=result["username"], email=result["email"])
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
#
# # роут для обновления информации о юзере по ID
# @app.put("/user/{user_id}", response_model=UserReturn)
# async def update_user(user_id: int, user: UserCreate):
#     query = "UPDATE users SET username = :username, email = :email WHERE id = :user_id"
#     values = {"user_id": user_id, "username": user.username, "email": user.email}
#     try:
#         await database.execute(query=query, values=values)
#         return {**user.dict(), "id": user_id}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to update user in database")
#
# Теперь, если отправить PUT-запрос:
#
# PUT http://localhost:8000/user/1
#
# {
#     "username": "updated_username",
#     "email": "updated_email@example.com"
# }
# То ответ будет таким:
#
# {
#     "username": "updated_username",
#     "email": "updated_email@example.com",
#     "id": 1
# }


#                                                Операция DELETE

# Операция "Удалить" включает в себя удаление записей данных из базы данных. В FastAPI вы можете обрабатывать операции
# удаления, обрабатывая запрос с уникальным идентификатором (например, ID) и удаляя соответствующую запись из базы
# данных.
#
# В целом как вы уже догадались, разницы особой не будет с предыдущей информацией, поэтому просто приведем
# демонстрационный код для HTTP-Delete запроса (интересует последний роут):
#
# from fastapi import FastAPI, HTTPException
# from databases import Database
# from pydantic import BaseModel
# from typing import Optional
#
# app = FastAPI()
#
# # URL для PostgreSQL (измените его под свою БД)
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
#
# database = Database(DATABASE_URL)
#
#
# # Модель User для валидации входных данных
# class UserCreate(BaseModel):
#     username: str
#     email: str
#
#
# # Модель User для валидации исходящих данных
# class UserReturn(BaseModel):
#     username: str
#     email: str
#     id: Optional[int] = None
#
#
# # тут устанавливаем условия подключения к базе данных и отключения
# @app.on_event("startup")
# async def startup_database():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown_database():
#     await database.disconnect()
#
#
# # создание роута для создания юзеров
# @app.post("/users/", response_model=UserReturn)
# async def create_user(user: UserCreate):
#     query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
#     values = {"username": user.username, "email": user.email}
#     try:
#         user_id = await database.execute(query=query, values=values)
#         return {**user.dict(), "id": user_id}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create user")
#
# # маршрут для получения информации о юзере по ID
# @app.get("/user/{user_id}", response_model=UserReturn)
# async def get_user(user_id: int):
#     query = "SELECT * FROM users WHERE id = :user_id"
#     values = {"user_id": user_id}
#     try:
#         result = await database.fetch_one(query=query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to fetch user from database")
#     if result:
#         return UserReturn(username=result["username"], email=result["email"])
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
#
# # роут для обновления информации о юзере по ID
# @app.put("/user/{user_id}", response_model=UserReturn)
# async def update_user(user_id: int, user: UserCreate):
#     query = "UPDATE users SET username = :username, email = :email WHERE id = :user_id"
#     values = {"user_id": user_id, "username": user.username, "email": user.email}
#     try:
#         await database.execute(query=query, values=values)
#         return {**user.dict(), "id": user_id}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to update user in database")
#
# # роут для удаления информации о юзере по ID
# @app.delete("/user/{user_id}", response_model=dict)
# async def delete_user(user_id: int):
#     query = "DELETE FROM users WHERE id = :user_id RETURNING id"
#     values = {"user_id": user_id}
#     try:
#         deleted_rows = await database.execute(query=query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to delete user from database")
#     if deleted_rows:
#         return {"message": "User deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="User not found")


#                                           Реализация CRUD-операций в FastAPI

# Чтобы реализовать операции CRUD в FastAPI, вам необходимо:
#
# Определите модель данных, которая представляет структуру ваших данных.
# Создайте необходимые конечные точки API (например, используя декораторы FastAPI) для каждой операции CRUD.
# Используйте запросы к базе данных (например, запросы на чистом SQL) для взаимодействия с базой данных и выполнения
# соответствующих операций.

#                                               Асинхронные операции CRUD

# Встроенная поддержка асинхронного программирования в FastAPI позволяет выполнять асинхронные операции CRUD для
# повышения производительности. Используя асинхронные запросы к базе данных (например, async SQLAlchemy
# (https://habr.com/ru/companies/otus/articles/683366/), Tortoise ORM, peewee-async и тп), вы можете эффективно
# управлять несколькими операциями с базой данных одновременно.
#
# FastAPI поддерживает различные драйверы асинхронных баз данных, например такие как asyncpg и databases.
#
# Использование асинхронных операций с базой данных в FastAPI дает несколько преимуществ:
#
# Повышенная производительность: асинхронные запросы к базе данных позволяют приложению обрабатывать несколько
# запросов одновременно, сокращая общее время отклика.
# Масштабируемость: Асинхронное программирование обеспечивает лучшее использование ресурсов и масштабируемость,
# облегчая работу с высокими параллельными нагрузками.
# Неблокирующее выполнение: Асинхронные операции с базой данных предотвращают блокировку приложения во время ожидания
# ответа базы данных, обеспечивая лучшую оперативность реагирования.
# Асинхронные операции с базой данных особенно полезны для обработки задач, связанных с вводом-выводом (I-O Bound) ,
# таких как выборка данных из удаленной базы данных.
#
# Для выполнения асинхронных запросов к базе данных мы используем асинхронные функции и выражения ожиданий (корутины
# и awaitable-объекты). Асинхронные функции (корутины), которые взаимодействуют с базой данных, обозначаются с
# использованием синтаксиса `async def`. В рамках этих функций мы можем использовать ключевое слово `await`, чтобы
# приостановить выполнение в ожидании завершения запроса к базе данных.

#                                               Обработка ошибок

# При реализации операций CRUD крайне важно корректно обрабатывать ошибки. FastAPI предоставляет надежные механизмы
# обработки ошибок, такие как создание соответствующих исключений HTTP (например, 404 Not found), когда запрашиваемый
# ресурс не существует или операция сталкивается с проблемой.
#
# Для сохранения целостности (консистентности) данных в вашей БД обязательно ознакомьтесь с "хорошими практиками"
# работы с БД. Например, если устанавливаете соединение с БД в каждом роутере каждый раз и используете ещё и
# синхронный подход, то обязательно делайте это через блок try/except. Не забудьте в блоке finally соединение закрыть.
#
# На этом уроке мы углубились в выполнение CRUD-операций с помощью FastAPI и узнали, как манипулировать данными в
# подключенной базе данных. Реализуя операции создания, чтения, обновления и удаления, вы можете создавать мощные
# веб-приложения, которые взаимодействуют с базами данных и обеспечивают бесперебойную функциональность управления
# данными. На следующем уроке мы рассмотрим миграцию баз данных с помощью Alembic, которая обеспечивает плавное
# обновление схемы базы данных и управление версиями


#                                                   ЗАДАЧА

# Структура проекта
# todo_pro/
# ├── config/
# │   └── config.py
# ├── db/
# │   └── db.py
# ├── models/
# │   └── models.py
# ├── routes/
# │   └── todo_resorces.py
# │── .env
# │── .env.example
# └── main.py

# config.py
# from dataclasses import dataclass
# from environs import Env
#
#
# @dataclass
# class Config:
#     db_url: str
#
#
# def load_config(path: str | None = None) -> Config:
#     env = Env()
#     env.read_env(path)
#     return Config(
#         db_url=env("DB_URL")
#     )

# db.py
# from fastapi import HTTPException
# from databases import Database
#
# from config.config import Config, load_config
# from models.models import CreateToDoRequest, UpdateToDoRequest, ToDo
#
# config: Config = load_config()
# database = Database(config.db_url)
#
#
# async def create_todo(todo: CreateToDoRequest) -> ToDo:
#     query = "INSERT INTO todo_list (title, description, completed) " \
#             "VALUES (:title, :description, :completed) RETURNING id;"
#     values = {"title": todo.title, "description": todo.description, "completed": False}
#     try:
#         todo_id = await database.execute(query=query, values=values)
#         return ToDo(**todo.model_dump(), id=todo_id)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create todo")
#
#
# async def get_todo(todo_id: int) -> ToDo:
#     query = "SELECT * FROM todo_list WHERE id=:todo_id"
#     values = {"todo_id": todo_id}
#     try:
#         result = await database.fetch_one(query=query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to fetch todo from database")
#     if result:
#         return ToDo(title=result["title"],
#                     description=result["description"],
#                     completed=result["completed"],
#                     id=result["id"])
#     else:
#         raise HTTPException(status_code=404, detail="Todo not found")
#
#
# async def update_todo(todo_id: int, todo: UpdateToDoRequest) -> ToDo:
#     query = "UPDATE todo_list " \
#             "SET title=:title, description=:description, completed=:completed " \
#             "WHERE id=:todo_id RETURNING id"
#     values = {"title": todo.title,
#               "description": todo.description,
#               "completed": todo.completed,
#               "todo_id": todo_id}
#     try:
#         result = await database.execute(query=query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to update todo in database")
#     if result:
#         return ToDo(**todo.model_dump(), id=todo_id)
#     else:
#         raise HTTPException(status_code=404, detail="Todo not found")
#
#
# async def delete_todo(todo_id: int) -> bool:
#     query = "DELETE FROM todo_list WHERE id=:todo_id RETURNING id"
#     values = {"todo_id": todo_id}
#     try:
#         deleted_rows = await database.execute(query, values=values)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to delete todo from database")
#     if deleted_rows:
#         return True
#     else:
#         raise HTTPException(status_code=404, detail="Todo not found")

# models.py
# from pydantic import BaseModel
#
#
# class CreateToDoRequest(BaseModel):
#     title: str
#     description: str
#
#
# class UpdateToDoRequest(BaseModel):
#     title: str
#     description: str
#     completed: bool = False
#
#
# class ToDo(BaseModel):
#     id: int
#     title: str
#     description: str
#     completed: bool = False

# todo_resource.py
# from fastapi import APIRouter
#
# from models.models import CreateToDoRequest, UpdateToDoRequest, ToDo
# from db.db import create_todo, get_todo, update_todo, delete_todo
#
# todos = APIRouter(prefix="/todos")
#
#
# @todos.post("/", response_model=ToDo)
# async def create(todo: CreateToDoRequest):
#     res = await create_todo(todo)
#     return res
#
#
# @todos.get("/{todo_id}", response_model=ToDo)
# async def read(todo_id: int):
#     res = await get_todo(todo_id)
#     return res
#
#
# @todos.put("/{todo_id}", response_model=ToDo)
# async def update(todo_id: int, todo: UpdateToDoRequest):
#     res = await update_todo(todo_id, todo)
#     return res
#
#
# @todos.delete("/{todo_id}", response_model=dict)
# async def delete(todo_id: int):
#     await delete_todo(todo_id)
#     return {"message": "Todo deleted successfully"}

# .env.example
# DB_URL=postgresql+asyncpg://user:password@localhost/mydb

# main.py
#
# import uvicorn
#
# from fastapi import FastAPI
# from contextlib import asynccontextmanager
#
# from db.db import database
# from routes.todo_resource import todos
#
#
# @asynccontextmanager
# async def lifespan(application: FastAPI):
#     await database.connect()
#     yield
#     await database.disconnect()
#
#
# app = FastAPI(lifespan=lifespan)
# app.include_router(todos)
#
# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=8000)


#                                                       5.3

#                                       Понимание процессов миграции баз данных

# Миграция баз данных необходима при разработке схемы базы данных с течением времени без потери существующих данных.
# По мере роста и изменения веб-приложений схема базы данных может нуждаться в обновлениях для соответствия новым
# функциям или требованиям к данным.
#
# Если вы даже не слышали об этом термине (что вряд ли, но вдруг), то можно прочитать вводную часть этой статьи
# (не обязательно читать до конца):
#
# https://habr.com/ru/articles/121265/
#
# Простыми словами, миграции БД - это аналог гитхаба, но для баз данных (хранится история изменений и можно откатиться
# назад, если что-то сломалось). В данном уроке мы рассмотрим эту проблематику, а не переезд БД из одного дата центра
# в другой или переход с MySQL на MongoDB (если кто так подумал).
#
# Alembic - это мощный инструмент миграции баз данных, который легко работает с FastAPI, позволяя вам управлять
# изменениями схемы базы данных контролируемым и версионным образом. Стоит отметить, что автором этого инструмента
# является автор SQLAlchemy, которая является одной из самых популярных ORM-ок в питоне. Поэтому покажем на примере
# этой ORM-ки.
#
# В зависимости от выбранной вами базы данных или ORM-ки к ней, рекомендуем поискать подходящий инструмент для
# работы, например peewee-migrations. В PonyORM миграции вышли между релизами 0.7.9 и 0.7.10, и они теперь идут
# из коробки" (и довольно удобны).

#                                              Начало работы с Alembic

# Чтобы начать использовать Alembic для миграции баз данных в вашем приложении FastAPI, вам необходимо выполнить
# следующие действия:
#
# Шаг 1: Установите Alembic
# Установите библиотеку Alembic, добавив ее в зависимости вашего проекта.
#
# pip install alembic
# Также вам может потребоваться синхронный драйвер базы данных, чтобы не танцевать с бубном для асинхронной работы
# Alembic'а, поэтому для постгреса установите psycopg2.
#
# Шаг 2: Инициализируйте Alembic
# Находясь в корне вашего FastAPI приложения, запустите консольную команду инициализации Alembic, чтобы создать
# необходимую структуру каталогов Alembic'а в вашем проекте.
#
# alembic init alembic
# Шаг 3: Настройте Alembic
# После инициализации Alembic создаст следующую структуру:
#
# your_project_directory/
#     alembic/
#         env.py
#         README
#         script.py.mako
#         versions/
#     alembic.ini
# Настройте Alembic в соответствии с настройками вашей базы данных, включая URL-адрес базы данных, драйвер и другие
# соответствующие сведения. В частности, вам (скорее всего, если ещё не создали) нужно будет определить модели таблиц
# (обычно модели таблиц отделены от Pydantic моделей и расположены где-нибудь в db/database.py), в которых не забыть
# указать на метаданные из SQLAlchemy, а также сконфигурировать env.py файл в соответствии с вашими настройками.
#
# Например так может выглядеть (можно заполнить, дополнив стандартные настройки) файл `alembic.ini`:
#
# [alembic]
# script_location = alembic
#
# [database]
# # Исправьте URL на настоящий для вашей БД
# sqlalchemy.url = DATABASE_URL
# Вот пример для Postgresql:
#
# [alembic]
# script_location = alembic
#
# [database]
# sqlalchemy.url = postgresql://user:password@localhost/dbname
# Пример env.py файла тут или тут (заодно можно прочитать подробнее про миграции).
#
# Стадию подготовки прошли.

#                                               Рабочий процесс Alembic

# Типичный рабочий процесс использования Alembic включает в себя следующие этапы:
#
# Шаг 1: Создайте миграцию
# Сгенерируйте новый сценарий миграции, используя интерфейс командной строки Alembic (CLI). Сценарий фиксирует
# изменения, которые необходимо внести в схему базы данных.
#
# Шаг 2: Просмотрите процесс миграции
# Проверьте сгенерированный сценарий миграции, чтобы убедиться, что он точно отражает предполагаемые изменения.
#
# Шаг 3: Примените миграцию
# Запустите команду Alembic для миграции, чтобы применить изменения к схеме базы данных. Head указывает, что
# эта миграция - "самый свежак", до самой последней версии. Можно указывать конкретный номер миграции, куда нужно
# мигрировать (тот, который revision), можно указывать на сколько миграций нужно продвинуться (+2 например), так как
# если было несколько миграций, которые не применены, то эта команда применит их все (по очереди).
#
# alembic upgrade head
# Шаг 4: Проверьте миграцию
# После применения миграции убедитесь, что схема базы данных была обновлена правильно.

#                                           Управление версиями и ревизии

# Alembic поддерживает таблицу версий в базе данных, отслеживая текущую версию миграции. Каждая миграция имеет
# никальный идентификатор редакции. Alembic использует эту информацию для определения порядка, в котором следует
# применять миграции или отменять их.

#                                                       Откаты

# Если миграция вызывает проблемы или ее необходимо отменить, и Alembic предоставляет механизм отката. Это позволяет
# вам отменить изменения, внесенные в результате конкретной миграции.
#
# Интеграция Alembic с FastAPI обеспечивает плавную эволюцию базы данных при сохранении существующих данных. Следуя
# рекомендациям по миграции баз данных, вы можете поддерживать надежную и масштабируемую структуру базы данных для
# вашего приложения FastAPI.
#
# В целом Alembic довольно мощная штука, поэтому при необходимости "боевого" применения лучше будет прочитать
# документацию (минус, что она на английском): https://alembic.sqlalchemy.org/en/latest/tutorial.html

#                                                   Задача на программирование

# Для выполнения этой задачи программирования вы настроите Alembic для миграции базы данных в приложении FastAPI и
# создадите простую миграцию для изменения схемы базы данных.
#
# Требования:
#
# 1. Установите Alembic и необходимый драйвер базы данных для выбранной вами базы данных (например, SQLite, PostgreSQL, MySQL).
#
# 2. Настройте Alembic, инициализировав его в вашем проекте FastAPI и настроив в соответствии с настройками вашей базы данных.
#
# 3. Создайте модель данных (модель SQLAlchemy), представляющую ресурс (например, объект "Product") с такими полями,
# как "id", "title", "price" и "count".
#
# 4. Сгенерируйте начальный сценарий миграции с помощью Alembic, который создает новую таблицу для объекта "Product".
#
# 5. Примените первоначальную миграцию к базе данных и убедитесь, что таблица "Product" создана.
#
# 6. Измените модель данных, добавив новое поле, например "description", к сущности "Product".
#
# 7. Сгенерируйте новый сценарий миграции с помощью Alembic, который отражает изменения в сущности "Product".
#
# 8. Примените новую миграцию к базе данных и убедитесь, что таблица "Product" теперь содержит поле "description".
#
# Примечание: Миграция базы данных является важным аспектом управления изменениями схемы базы данных в реальных
# приложениях. Эта задача предоставляет упрощенный сценарий, и в производственной среде вы должны следовать
# дополнительным рекомендациям, обрабатывать миграцию данных и учитывать возможные сценарии потери данных. Если вам
# привычнее работать в другим технологическим стеком, то изучите возможность выполнить задание (миграцию БД)
# подходящим для вас способом.

