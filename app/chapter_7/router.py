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

#                                                       7.2

#                                   Введение мокинг (подделку) внешних зависимостей

# В приложениях FastAPI внешние зависимости, такие как базы данных, внешние API-интерфейсы или сторонние сервисы,
# играют решающую роль в предоставлении дополнительной функциональности. Однако при написании модульных тестов мы
# хотим изолировать тестируемый код от этих внешних зависимостей. Имитация (подделка, мокинг) внешних зависимостей
# позволяет нам заменять реальные реализации контролируемыми заменителями, гарантируя, что наши тесты фокусируются
# исключительно на конкретной тестируемой единице кода.

#                                                   Потребность в мокинге

# Модульные тесты должны быть быстрыми, надежными и повторяемыми. Без мокинга модульные тесты могут замедлиться из-за
# времени, затрачиваемого на взаимодействие с реальными базами данных или API. Более того, опора на реальные
# реализации может привести к несогласованным результатам тестирования из-за внешних факторов, таких как доступность
# сети или изменения данных.

#                                        Использование `unittest.mock` для мокинга

# Встроенная в Python библиотека unittest.mock предоставляет мощные инструменты для мокинга над объектами и функциями.
# С помощью `unittest.mock` мы можем создавать макетные объекты, которые имитируют поведение реальных объектов или
# функций, что делает их подходящей заменой внешних зависимостей в модульных тестах.

#                                               Замена внешних зависимостей

# В FastAPI внешние зависимости часто внедряются в конечные точки или службы с помощью внедрения зависимостей.
# Заменяя эти зависимости фиктивными объектами во время модульных тестов, мы можем контролировать данные и поведение,
# которые они предоставляют, что позволяет нам более эффективно тестировать различные сценарии.
#
# Допустим, у нас есть часть кода, которая что-то делает с внешним API:
#
# # external_api.py
#
# import requests
#
# def fetch_data_from_api():
#     response = requests.get("https://api.example.com/data")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
#
# def process_data(data):
#     # какая-то логика обработки данных
#     return data.upper()
# И потом мы эти данные как-то обрабатываем в основном приложении:
#
# # app.py
#
# from external_api import fetch_data_from_api, process_data
#
# def get_and_process_data():
#     data = fetch_data_from_api()
#     if data:
#         return process_data(data)
#     else:
#         return None
# Давайте напишем юнит-тест для get_and_process_data функции, используя unittest.mock:
#
# # test_app.py
#
# import unittest
# from unittest.mock import patch, MagicMock
# from app import get_and_process_data
#
# class TestApp(unittest.TestCase):
#
#     @patch("app.fetch_data_from_api")
#     @patch("app.process_data")
#     def test_get_and_process_data(self, mock_process_data: MagicMock, mock_fetch_data: MagicMock):
#         # Mock функции fetch_data_from_api для возврата "sample response"
#         mock_response = {"key": "value"}
#         mock_fetch_data.return_value = mock_response
#
#         # Mock функции process_data
#         mock_processed_data = {"KEY": "VALUE"}
#         mock_process_data.return_value = mock_processed_data
#
#         # вызываем тестируемую функцию
#         result = get_and_process_data()
#
#         # Assertions
#         mock_fetch_data.assert_called_once()  # убеждаемся, что fetch_data_from_api был вызван
#         mock_process_data.assert_called_once_with(mock_response)  # убеждаемся, что process_data была вызвана с
#         "mocked response"
#         self.assertEqual(result, mock_processed_data)  # убеждаемся, что функция вернула ожидаемые обработанные
#         данные
# В приведенном выше тесте мы использовали декоратор `patch` для имитации функций `fetch_data_from_api` и
# `process_data`. Мы также создали фиктивные возвращаемые значения для обеих функций, используя `return_value`.
# При такой настройке фактические функции `fetch_data_from_api` и `process_data` заменяются фиктивными объектами во
# время выполнения теста. Затем мы можем утверждать, что эти поддельные функции были вызваны правильно и что функция
# `get_and_process_data` ведет себя так, как ожидалось. Используя `unittest.mock`, мы можем изолировать наши модульные
# тесты от внешних зависимостей, делая их более надежными и быстрыми.

#                                            Лучшие практики для мокинга

# Хотя мокинг является мощным инструментом для модульного тестирования, его следует использовать разумно. Чрезмерное
# использование макетов или написание тестов, тесно связанных с деталями реализации, может привести к хрупким тестам,
# которые легко ломаются при изменении кода. Поэтому важно следовать лучшим практикам и разрабатывать тестируемый код
# для достижения надежных и поддерживаемых модульных тестов.

#                                            Исправление внешних функций

# Одним из распространенных вариантов использования mocking в FastAPI является исправление внешних функций, которые
# взаимодействуют с базами данных или API. Исправляя эти функции, мы можем контролировать их возвращаемые значения
# или моделировать различные ответы, обеспечивая всесторонний охват тестированием.

#                                               Проверка вызовов функций

# В дополнение к замене внешних зависимостей, мы также можем проверить, что определенные функции или методы вызываются
# во время модульных тестов. Это полезно для обеспечения того, чтобы определенные действия или запросы выполнялись
# должным образом в тестируемом коде.
#
# Библиотека `unittest.mock` предоставляет `assert_called_once`, `assert_called_with` и другие методы утверждения,
# которые позволяют вам проверить, была ли вызвана функция или метод с определенными аргументами.
#
# Давайте модифицируем предыдущий код для демонстрации, объединив для читаемости external_api.py и app.py:
#
# # main.py
#
# from fastapi import FastAPI, Depends
# import requests
#
# app = FastAPI()
#
# # Внешний API URL (для демонстрации процесса обратимся сами к себе, но тут должен быть реальный)
# EXTERNAL_API_URL = "https://catfact.ninja/fact"
#
#
# # функция для получения данных из внешнего API
# def fetch_data_from_api():
#     response = requests.get(EXTERNAL_API_URL)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
#
#
# # функция для обработки данных
# def process_data(data):
#     # как-то логика обработки данных
#     new_data = {}
#     for key, value in data.items():
#         new_data[key.upper()] = value.upper()
#     return new_data
#
#
# # роут, который извлекает и обрабатывает данные от внешнего API
# @app.get("/data/")
# async def get_and_process_data():
#     data: dict = fetch_data_from_api()
#     if data:
#         return process_data(data)
#     else:
#         return {"error": "Failed to fetch data from the external API"}
# Теперь давайте напишем модульный тест, чтобы убедиться, что функции `fetch_data_from_api` и `process_data`
# вызываются во время выполнения конечной точки `/data/`:
#
# # test_main.py
#
# import unittest
# from fastapi.testclient import TestClient
# from main import app, fetch_data_from_api, process_data
# from unittest.mock import patch
#
# client = TestClient(app)
#
#
# class TestMain(unittest.TestCase):
#
#     @patch("main.fetch_data_from_api")
#     @patch("main.process_data")
#     def test_get_and_process_data(self, mock_process_data, mock_fetch_data):
#         # Имитируем функцию fetch_data_from_api, чтобы вернуть пример ответа
#         mock_response = {"key": "value"}
#         mock_fetch_data.return_value = mock_response
#
#         # имитируем функцию process_data
#         mock_processed_data = {"KEY": "VALUE"}
#         mock_process_data.return_value = mock_processed_data
#
#         # отправляем запрос на конечную точку /data/
#         response = client.get("/data/")
#
#         # наши assertions
#         mock_fetch_data.assert_called_once()  # Убеждаемся, что fetch_data_from_api был вызван один раз
#         mock_process_data.assert_called_once_with(mock_response)  # убеждаемся, что process_data был вызван
#         с "mocked response"
#         self.assertEqual(response.status_code, 200)  # проверяем что status code равен 200
#         self.assertEqual(response.json(), mock_processed_data)  # проверяем, что данные ответа соответствуют
#         имитируемым обработанным данным
# В тесте мы используем декоратор `@patch`, чтобы заменить функции `fetch_data_from_api` и `process_data` фиктивными
# объектами. Затем мы используем метод `assert_called_once`, чтобы убедиться, что каждая функция вызывается ровно
# один раз во время выполнения конечной точки `/data/`.
#
# Метод `assert_called_once_with` используется для проверки того, что функция `process_data` вызывается с ожидаемым
# аргументом `mock_response`.
#
# Используя эти методы утверждения (assertions), мы можем подтвердить, что желаемые функции вызываются с ожидаемыми
# аргументами, гарантируя, что код ведет себя так, как задумано во время модульных тестов.

#                                                   ЗАДАЧА

# Для этой задачи программирования вам нужно написать модульные тесты для приложения FastAPI, которое включает в себя
# имитацию внешних зависимостей.
#
# Требования:
#
# 1. Настройте приложение FastAPI по крайней мере с двумя конечными точками API, которые взаимодействуют с внешними
# зависимостями (например, с базой данных или внешним API).
#
# 2. Определите внешние функции или API-интерфейсы, которые необходимо имитировать во время модульного тестирования.
# Создайте план того, какие данные и ответы должны предоставлять эти макеты.
#
# 3. Напишите модульные тесты с использованием pytest для конечных точек, которые взаимодействуют с внешними
# зависимостями. Используйте библиотеку `unittest.mock` для создания макетных объектов (заглушек) и исправления
# внешних функций.
#
# 4. Убедитесь, что модульные тесты охватывают различные сценарии и пограничные случаи, включая случаи, когда внешние
# функции возвращают неожиданные данные или вызывают исключения.
#
# 5. Убедитесь, что тестируемый код корректно взаимодействует с имитируемыми внешними зависимостями и соответствующим
# образом обрабатывает ответы.
#
# 6. Следуйте рекомендациям по модульному тестированию и избегайте чрезмерного использования макетов. Разработайте
# тестируемый код, чтобы модульные тесты были удобными в обслуживании и надежными.
#
# Примечание: Используйте `unittest.mock.patch` или `unittest.mock.patch.object` для исправления внешних зависимостей
# в ваших модульных тестах. Фреймворк `pytest` и плагин `pytest-asyncio` рекомендуются для написания асинхронных
# модульных тестов в FastAPI.

#                                                   Вариант 1

# """external_api.py"""
# import requests
#
#
# EXTERNAL_API_URL = "https://catfact.ninja"
#
#
# def fetch_random_fact() -> dict or None:
#     response = requests.get(f"{EXTERNAL_API_URL}/fact", timeout=10)
#     if response.status_code == 200:
#         return response.json()
#     return None
#
#
# def process_fact(data) -> str or None:
#     if data:
#         return data.get("fact")
#     return None
#
#
# def fetch_last_page() -> dict or None:
#     response = requests.get(f"{EXTERNAL_API_URL}/facts", timeout=10)
#     if response.status_code == 200:
#         return response.json()
#     return None
#
#
# def process_last_page(data) -> int or None:
#     if data:
#         return {key: val for key, val in data.items() if key in ('last_page')}
#     return None
# """main.py"""
# from fastapi import FastAPI
# from external_api import (fetch_random_fact, process_fact, fetch_last_page,
# process_last_page)
#
#
# app = FastAPI()
#
#
# @app.get("/random_fact")
# async def get_random_fact():
#     data: dict = fetch_random_fact()
#     if data:
#         return {"random_fact": process_fact(data)}
#     return {"error": "Failed to fetch data from the external API"}
#
#
# @app.get("/last_page")
# async def get_last_page():
#     data: dict = fetch_last_page()
#     if data:
#         return process_last_page(data)
#     return {"error": "Failed to fetch data from the external API"}
# """test_main.py"""
# import unittest
# from unittest.mock import patch
# from fastapi.testclient import TestClient
# from main import (app, fetch_random_fact, process_fact, fetch_last_page,
# process_last_page)
#
#
# client = TestClient(app)
#
#
# class TestMain(unittest.TestCase):
#     @patch("main.fetch_random_fact")
#     @patch("main.process_fact")
#     def test_get_and_process_fact(self, mock_process_data, mock_fetch_data):
#         mock_response = {"fact":"value","length":5}
#         mock_fetch_data.return_value = mock_response
#
#         mock_processed_data = "value"
#         mock_process_data.return_value = mock_processed_data
#
#         response = client.get("/random_fact")
#
#         mock_fetch_data.assert_called_once()
#         mock_process_data.assert_called_once_with(mock_response)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"random_fact": "value"})
#
#     @patch("main.fetch_last_page")
#     @patch("main.process_last_page")
#     def test_get_and_process_last_page(self, mock_process_data, mock_fetch_data):
#         mock_response = {
#             "current_page":1,
#             "data":[{"fact":"value","length":5}],
#             "first_page_url":"https:\\catfact.ninja\facts?page=1",
#             "from":1,
#             "last_page":34,
#             "last_page_url":"https:\\catfact.ninja\facts?page=34",
#             "links":[],
#             "next_page_url":"https:\\catfact.ninja\facts?page=2",
#             "path":"https:\\catfact.ninja\facts",
#             "per_page":10,
#             "prev_page_url": None,
#             "to":10,
#             "total":332
#         }
#         mock_fetch_data.return_value = mock_response
#
#         mock_processed_data = {"last_page":34}
#         mock_process_data.return_value = mock_processed_data
#
#         response = client.get("/last_page")
#
#         mock_fetch_data.assert_called_once()
#         mock_process_data.assert_called_once_with(mock_response)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), mock_processed_data)

