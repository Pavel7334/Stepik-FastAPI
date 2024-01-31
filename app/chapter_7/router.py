from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["Chapter_7:"]
)

#                                                   7.1

#                                       Написание модульных тестов для FastAPI

# На этом уроке мы рассмотрим важность модульного тестирования в приложениях FastAPI и узнаем, как писать модульные
# тесты для обеспечения корректности и надежности наших веб-API. Тестирование является важной частью процесса
# разработки, поскольку оно помогает выявлять и исправлять ошибки на ранней стадии, что приводит к созданию более
# надежной и поддерживаемой кодовой базы.

#                                        Что такое модульное тестирование?

# Модульное тестирование - это процесс изолированного тестирования отдельных модулей или компонентов программного
# приложения для проверки того, что каждый модуль работает должным образом. В контексте FastAPI единицей измерения
# может быть отдельная конечная точка, модель данных или конкретная функция в вашем API. Написание модульных тестов
# позволяет нам выявлять и исправлять проблемы в изолированных компонентах, что облегчает поиск и устранение проблем в
# кодовой базе.

#                                               Настройка тестовой среды

# Прежде чем мы приступим к написанию тестов, давайте настроим тестовую среду. FastAPI легко работает с популярными
# фреймворками тестирования, такими как Pytest. Убедитесь, что в вашей среде разработки установлен Pytest.
#
# pip install pytest
# Теперь давайте создадим новый каталог с именем "tests" в корне вашего проекта FastAPI. Pytest автоматически
# обнаружит и запустит тесты в этом каталоге. Ищутся файлы с именами «test_*.py» или «*_test.py».

#                                       Написание Вашего первого модульного теста

# Предположим, у нас есть простое приложение FastAPI с конечной точкой, которая вычисляет сумму двух чисел. Конечная
# точка определяется следующим образом:
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/sum/")
# def calculate_sum(a: int, b: int):
#     return {"result": a + b}
# Чтобы написать модульный тест для этой конечной точки, создайте новый файл Python в каталоге "tests", например,
# "test_app.py". В этом файле мы импортируем приложение FastAPI и будем использовать встроенные инструменты для
# тестирования.
#
# from fastapi.testclient import TestClient
# from my_app import app
#
# client = TestClient(app)
#
# def test_calculate_sum():
#     response = client.get("/sum/?a=5&b=10")
#     assert response.status_code == 200
#     assert response.json() == {"result": 15}
# В приведенном выше тесте мы используем класс `TestClient` из FastAPI для имитации запроса к конечной точке "/sum/"
# с параметрами "a=5" и "b=10". Затем мы утверждаем, что код состояния ответа равен 200 (OK) и что ответ JSON
# соответствует ожидаемому результату.
#
# Или попродвинутее (правда этот пример составлялся на Python 3.9 с Pydantic 1.10.7 - да, на смартфоне такие древние
# либы :) Для более свежей версии посмотрите комментарии, не будем переписывать пример, ибо суть, надеемся, понятна):
#
# from fastapi.testclient import TestClient
# from my_app import app  # включаем сюда ваш инстанс FastAPI приложения с названием "app"
#
# # создаём инстанс TestClient для тестирования FastAPI приложения
# client = TestClient(app)
#
# def test_calculate_sum():
#     # Test case 1: валидные входные данные
#     response = client.get("/sum/?a=5&b=10")
#     assert response.status_code == 200
#     assert response.json() == {"result": 15}
#
#     # Test case 2: отрицательные числа
#     response = client.get("/sum/?a=-8&b=-3")
#     assert response.status_code == 200
#     assert response.json() == {"result": -11}
#
#     # Test case 3: ноль и положительное число
#     response = client.get("/sum/?a=0&b=7")
#     assert response.status_code == 200
#     assert response.json() == {"result": 7}
#
#     # Test case 4: одно число не введено
#     response = client.get("/sum/?a=3")
#     assert response.status_code == 422  # Unprocessable Entity (validation error)
#     assert response.json() == {
#         "detail": [
#             {
#                 "loc": ["query", "b"],
#                 "msg": "field required",
#                 "type": "value_error.missing"
#             }
#         ]
#     }
# Запуск тестов:
#
# Чтобы запустить тесты, откройте свой терминал, перейдите в корневой каталог проекта и выполните следующую команду:
#
# pytest
# Pytest автоматически обнаружит и выполнит все тесты в каталоге "tests". Если все настроено правильно, вы должны
# увидеть сообщение, указывающее на то, что тест пройден.

#                                                       ЗАДАЧА

# Для этой задачи программирования вам необходимо написать модульные тесты для приложения FastAPI, которое включает в
# себя несколько конечных точек и функциональных возможностей.
#
# Требования:
#
# 1. Настройте приложение FastAPI как минимум с тремя конечными точками API (например, одна для регистрации
# пользователя, одна для извлечения данных и одна для удаления данных).
#
# 2. Напишите модульные тесты для каждой конечной точки с помощью pytest. Протестируйте различные сценарии и крайние
# случаи, чтобы обеспечить всесторонний охват тестированием.
#
# 3. Для каждого тестового примера используйте `TestClient` для отправки HTTP-запросов на соответствующую конечную
# точку и проверки кода состояния ответа и данных с помощью утверждений (assert).
#
# 4. Организуйте связанные тестовые примеры в отдельные тестовые функции или тестовые классы для удобства
# сопровождения и чтения.
#
# 5. Реализуйте по крайней мере один тестовый пример, который включает в себя имитацию внешней зависимости (например,
# подключение к базе данных или внешний API) для создания контролируемой тестовой среды.
#
# 6. Убедитесь, что модульные тесты прошли успешно, указывая на то, что конечные точки API и функциональные
# возможности работают должным образом.
#
# После выполнения задачи у вас должен быть набор модульных тестов, которые тщательно проверяют функциональность
# вашего приложения FastAPI. Выполнение тестов с помощью pytest должно привести к прохождению всех тестовых примеров,
# что указывает на надежность вашего приложения и отсутствие критических ошибок.
#
# Примечание: Вы можете использовать фреймворк `pytest` и плагин `pytest-asyncio` для написания асинхронных модульных
# тестов в FastAPI.

#                                                 Вариант 1

# Модель:
#
# class User(BaseModel):
#     username: str
#     email: EmailStr
#     password: constr(min_length=4, max_length=8)
#
# Конечные точки:
#
# users_db = {}
#
# @app.post("/register")
# async def create_user(user: User):
#     if user.username in users_db:
#         raise HTTPException(
#             detail="Имя пользователя уже занято",
#             status_code=400
#         )
#     users_db[user.username] = user
#     return {"message": "User registered successfully"}
#
#
# @app.get("/user/{username}")
# async def get_user(username: str):
#     if username not in users_db:
#         raise HTTPException(
#             detail="Пользователь с таким именем не существует",
#             status_code=404
#         )
#     return {"user": users_db[username]}
#
#
# @app.delete("/user/{username}")
# async def delete_user(username: str):
#     if username not in users_db:
#         raise HTTPException(
#             detail="Пользователь с таким именем не существует",
#             status_code=404
#         )
#     deleted_user = users_db.pop(username)
#     return {"message": "Пользователь успешно удален", "deleted_user": deleted_user}
#
# Тесты:
#
# @patch("main.users_db", {})
# def test_register_user():
#     response = client.post(
#         "/register", json={"username": "Egor", "email": "egor@example.com", "password": "1234"}
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "User registered successfully"}
#
#     response = client.post(
#         "/register", json={"username": "Egor", "email": "egor@example.com", "password": "1234"}
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Имя пользователя уже занято"}
#
#
# def test_get_user():
#     users_db["Egor"] = {"username": "Egor", "email": "egor@example.com", "password": "1234"}
#     response = client.get("/user/Egor")
#     assert response.status_code == 200
#     assert response.json() == {"user": {"username": "Egor", "email": "egor@example.com", "password": "1234"}}
#
#     response = client.get("/user/nonexistentuser")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Пользователь с таким именем не существует"}
#
#
# def test_delete_user():
#     users_db["Egor"] = {"username": "Egor", "email": "egor@example.com", "password": "1234"}
#     response = client.delete("/user/Egor")
#     assert response.status_code == 200
#     assert response.json() == {
#         "message": "Пользователь успешно удален",
#         "deleted_user": {"username": "Egor", "email": "egor@example.com", "password": "1234"}
#     }
#     assert "Egor" not in users_db
#
#     response = client.delete("/user/nonexistentuser")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Пользователь с таким именем не существует"}

#                                                  Вариант 2

# app/main.py
#
# import uvicorn
#
# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel, EmailStr
# from typing import Optional
#
# app = FastAPI()
#
#
# class Contact(BaseModel):
#     id: Optional[int] = None
#     name: str
#     email: EmailStr
#     phone: str
#
#
# contacts_db: dict[int, Contact] = {}
#
#
# def id_generator():
#     counter = max(contacts_db.keys()) if contacts_db else 0
#     while True:
#         counter += 1
#         yield counter
#
#
# id_gen = id_generator()
#
#
# def _check_contact(contact: Contact):
#     errors = []
#     for db_contact in contacts_db.values():
#         if contact.name == db_contact.name:
#             errors.append(f"name={contact.name} already taken")
#         if contact.email == db_contact.email:
#             errors.append(f"email={contact.email} already taken")
#
#     if len(errors) > 0:
#         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=", ".join(errors))
#
#
# @app.post("/contacts/", response_model=Contact, status_code=status.HTTP_201_CREATED)
# def create_contact(contact: Contact):
#     _check_contact(contact)
#     contact.id = next(id_gen)
#     contacts_db[contact.id] = contact
#     return contact
#
#
# @app.get("/contacts/{id}", response_model=Contact, status_code=status.HTTP_200_OK)
# def get_contact(id: int):
#     if id not in contacts_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Contact with id={id} not found")
#     return contacts_db[id]
#
#
# @app.delete("/contacts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_contact(id: int):
#     if id not in contacts_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Contact with id={id} not found")
#     del contacts_db[id]
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
#
# tests/test_main.py
# from fastapi import status
# from fastapi.testclient import TestClient
#
# from app.main import app, Contact, contacts_db
#
# client = TestClient(app)
#
#
# def test_create_contact():
#     contact_json = {
#         "name": "newer",
#         "email": "newer@mail.com",
#         "phone": "111-22-33"
#     }
#
#     response = client.post("/contacts/", json=contact_json)
#
#     assert response.status_code == status.HTTP_201_CREATED
#
#     response_json = response.json()
#     assert response_json["id"] is not None
#     del response_json["id"]
#     assert response_json == contact_json
#
#
# def test_create_contact_repeatedly():
#     contact_json = {
#         "name": "double",
#         "email": "double@mail.com",
#         "phone": "111-22-33"
#     }
#
#     response = client.post("/contacts/", json=contact_json)
#     assert response.status_code == status.HTTP_201_CREATED
#
#     response = client.post("/contacts/", json=contact_json)
#     assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
#
#
# def test_create_contact_missing_field():
#     missing_json = {
#         "name": "double",
#         "email": "double@mail.com"
#     }
#
#     response = client.post("/contacts/", json=missing_json)
#     assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
#
#
# def test_get_contact():
#     id = 999999999
#     contact = Contact(id=id, name="Ivan", email="ivan@domen.org", phone="999-99-00")
#     contacts_db[id] = contact
#
#     response = client.get(f"contacts/{id}")
#
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == contact.model_dump()
#
#     del contacts_db[id]
#
#
# def test_get_contact_not_found():
#     id = 999999991
#
#     response = client.get(f"contacts/{id}")
#
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#
#
# def test_delete_contact():
#     id = 999999999
#     contact = Contact(id=id, name="Ivan", email="ivan@domen.org", phone="999-99-00")
#     contacts_db[id] = contact
#
#     response = client.delete(f"contacts/{id}")
#
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#
#
# def test_delete_contact_not_fount():
#     id = 999999991
#
#     response = client.delete(f"contacts/{id}")
#
#     assert response.status_code == status.HTTP_404_NOT_FOUND