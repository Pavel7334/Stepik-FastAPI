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

#                                                     7.3

#                                         Введение в интеграционное тестирование

# Интеграционное тестирование в FastAPI включает в себя тестирование взаимодействий между различными частями вашего
# приложения. В отличие от модульных тестов, которые фокусируются на отдельных блоках кода, интеграционные тесты
# гарантируют, что интегрированные компоненты работают вместе должным образом. Интеграционные тесты помогают выявить
# проблемы, которые могут возникнуть при взаимодействии нескольких компонентов, такие как проблемы с зависимостями,
# подключениями к базе данных или интеграцией API.

#                                     Использование TestClient для интеграционных тесто

# FastAPI предоставляет класс `TestClient` из модуля `fastapi.testclient`, который является ценным инструментом для
# запуска интеграционных тестов. "TestClient" позволяет вам выполнять реальные HTTP-запросы к вашему приложению
# FastAPI во время тестирования, имитируя реальные сценарии.
#
# Что также немаловажно, TestClient позволяет тестировать приложение FastAPI без его запуска, имитируя реальные
# запросы (без запуска uvicorn'а).
#
# Для асинхронных тестов можно использовать AsyncClient из модуля httpx.

#                                              Подготовка тестовой среды

# Перед запуском интеграционных тестов с помощью `TestClient` крайне важно настроить тестовую среду, которая очень
# похожа на производственную, но с контролируемыми данными. Это может включать в себя создание тестовой базы данных,
# заполнение ее тестовыми данными и настройку любых необходимых зависимостей.

#                                       Тестирование конечных точек и маршрутов

# нтеграционные тесты с "TestClient" позволяют вам тестировать конечные точки API вашего приложения и маршруты
# точно так же, как это сделал бы реальный пользователь или внешняя служба. Отправляя HTTP-запросы и получая ответы,
# вы можете убедиться, что ваш API ведет себя корректно в различных условиях.
#
# Вот пример того, как вы можете выполнить интеграционное тестирование с помощью `TestClient`.
#
# Предположим, у вас есть приложение FastAPI со следующим кодом:
#
# # main.py
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}
# Теперь давайте напишем интеграционный тест, используя `TestClient`, чтобы протестировать конечную
# точку `/items/{item_id}`:
#
# # test_main.py
#
# from fastapi.testclient import TestClient
# from main import app
#
# client = TestClient(app)
#
# def test_read_item():
#     # Отправляем запрос на конечную точку /items/{item_id} с item_id=1
#     response = client.get("/items/1")
#
#     # Assertions
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1}
#
#     # Отправляем запрос на конечную точку /items/{item_id} с item_id=z (неправильный тип данных)
#     response = client.get("/items/z")
#
#     # Assertions
#     assert response.status_code == 200  # Это завершится ошибкой, поскольку конечная точка не обработает наш
#     тип данных
#     assert response.json() == {"item_id": "z"}  # это тоже завершится ошибкой по той же причине
# В этом примере мы сначала импортируем `TestClient` и наше приложение FastAPI из `main.py`. Затем мы создаем объект
# `TestClient` с помощью нашего приложения FastAPI.
#
# Функция `test_read_item` выполняет два тестовых примера:
#
# Он отправляет запрос GET в `/items/1` и проверяет, что код состояния ответа равен 200, а ответ в формате JSON
# соответствует ожидаемому результату `{"item_id": 1}`.
# Он отправляет запрос GET на `/items/z` (неправильный item_id) и вызывает ошибочный assertion, что код статуса
# ответа равен 200, а ответ в формате JSON равен `{"item_id": "z"}`. Этот тест завершится неудачей.
# Или расширенный пример интеграционного теста, но тоже упрощенный.
#
# Для примера есть приложение:
#
# # main.py
# from fastapi import FastAPI, HTTPException, Request, Response
# from pydantic import BaseModel
#
#
# app = FastAPI()
#
# # псевдо-бд
# fake_users_db = [
#     {
#         "user_id": 1,
#         "username": "user123",
#         "password": "secretpassword",
#         "email": "user@example.com"
#     }
# ]
#
# # имитируем хранилище сессий
# sessions = {}
#
#
# # модельки
# class UserCredentials(BaseModel):
#     username: str
#     password: str
#
# class UserData(BaseModel):
#     user_id: int
#     username: str
#     email: str
#
#
# # роуты
# @app.post("/login/") # проверяем наличие юзера и возвращаем куки
# def login(user_creds: UserCredentials, response: Response):
#     for user in fake_users_db:
#         if user["username"] == user_creds.username and user["password"] == user_creds.password:
#             response.set_cookie(key="session_cookie", value="my_random_cookie")
#             sessions[user_creds.username] = "my_random_cookie" # это чисто для демонстрации, если 5 юзеров зайдут,
#             то всем не нужно одинаковые куки ставить
#             return {"message": "Login successful"}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#
#
# @app.get("/protected_data/", response_model=UserData) # возвращаем данные по кукам, если они валидны
# def protected_data(request: Request):
#     for username, cookie in sessions.items():
#         if request.cookies.get("session_cookie") and cookie == request.cookies.get("session_cookie"):
#             user = get_user_by_username(username)
#             return UserData(**user)
#     raise HTTPException(status_code=401, detail="Bad cookie")
#
#
# def get_user_by_username(username: str): # вспомогательная функция по извлечению юзера из БД
#     for user in fake_users_db:
#         if user.get("username") == username:
#             return user
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
# Тогда интеграционный тест мог бы быть таким:
#
# # test_app.py
# from fastapi.testclient import TestClient
# from main import app # тут замените импорт на правильное расположение файла
#
#
# client = TestClient(app)
#
# def test_login_and_access_data():
#     # тестируем точку логина, направляя учетные данные и получая куки
#     login_data = {
#         "username": "user123",
#         "password": "secretpassword"
#     }
#     response = client.post("/login/", json=login_data)
#     assert response.status_code == 200
#     assert "set-cookie" in response.headers
#
#     # извлекаем куки из ответа
#     cookies = response.cookies
#     cookie_value = cookies["session_cookie"]
#
#     # проверяем доступ к получению информации через полученные куки
#     headers = {
#         "Cookie": f"session_cookie= {cookie_value}"
#     }
#     response = client.get("/protected_data/", headers=headers)
#     assert response.status_code == 200
#     data = response.json()
#     assert "user_id" in data
#     assert "username" in data
#     assert "email" in data
#
# Мы, конечно, можем быть более тщательными, проверять разное поведение юзеров (в т.ч. неблагонадежное). Тут мы не
# проверяем подмену данных, крайние значения и прочее. Но главное понять идею - что мы можем имитировать действия
# пользователя (что он послал, что ему пришло, какой ответ дала база данных, записались ли значения, и прочее и прочее)
# . То есть отличие интеграционного теста от модульного в том, что при интеграционном тестировании мы проверяем, как
# приложение работает в совокупности.
#
# Интеграционное тестирование с помощью "TestClient" позволяет вам проверить поведение всего вашего приложения
# FastAPI, включая его маршруты и взаимодействия с внешними зависимостями, в тестовой среде. Это гарантирует, что
# конечные точки реагируют должным образом, и помогает вам выявить любые потенциальные проблемы в вашем приложении.

#                                       Тестирование аутентификации и авторизации

# Интеграционные тесты также полезны для тестирования механизмов аутентификации и авторизации в вашем приложении
# FastAPI. Вы можете смоделировать сценарии, в которых пользователи или службы имеют разные роли и разрешения,
# чтобы обеспечить надлежащий контроль доступа.

#                                       Целостность данных и тестирование базы данных

# Для приложений с интеграцией баз данных интеграционные тесты могут проверять целостность данных и тестировать
# различные операции CRUD. Вы можете создавать тестовые данные, выполнять операции с базой данных и проверять
# правильность извлечения и обновления данных.

#                                       Тестирование непрерывной интеграции (CI)

# Интеграционные тесты часто включаются в процесс непрерывной интеграции (CI). Тестирование CI включает в себя запуск
# автоматических тестов всякий раз, когда изменения передаются в репозиторий кода. Такая практика помогает выявлять
# проблемы на ранней стадии и гарантирует, что изменения не нарушат существующие функциональные возможности.

#                                         Управление тестовыми базами данных

# Для поддержания изоляции и контроля во время интеграционных тестов обычно используется отдельная тестовая база
# данных. Вы можете настроить свое приложение так, чтобы оно использовало тестовую базу данных во время тестирования,
# и сбрасывать ее перед каждым тестом, чтобы обеспечить чистый лист для каждого тестового примера.

#                                                   ЗАДАЧА

# Для этой задачи программирования вам нужно написать интеграционные тесты, используя "TestClient" для приложения
# FastAPI с интеграцией с базой данных.
#
# Требования:
#
# 1. Настройте приложение FastAPI с интеграцией с базой данных (например, SQLite, PostgreSQL или MySQL).
#
# 2. Подготовьте тестовую среду, создав отдельную тестовую базу данных. Настройте свое приложение так, чтобы оно
# использовало эту тестовую базу данных во время интеграционного тестирования.
#
# 3. Внедрите по крайней мере три конечные точки API с различными функциональными возможностями, такими как
# регистрация пользователей, извлечение данных и обновление данных.
#
# 4. Напишите интеграционные тесты, используя pytest и `TestClient` для тестирования конечных точек API. Убедитесь,
# что тесты охватывают различные сценарии, включая положительные случаи и сценарии потенциальных ошибок.
#
# 5. Протестируйте поведение конечной точки в различных условиях, таких как отправка неверных данных, проверки
# подлинности и авторизации, а также пограничные случаи.
#
# 6. Убедитесь, что интеграционные тесты корректно взаимодействуют с приложением и базой данных, выполняя операции
# CRUD должным образом.
#
# 7. Включите по крайней мере один тест, который проверяет поведение механизмов аутентификации и авторизации в вашем
# приложении.
#
# Примечание: Для выполнения этой задачи вы можете использовать подходящий компонент database engine, такой как SQLite
# или PostgreSQL, для вашей тестовой среды. Не забудьте сбросить тестовую базу данных перед каждым тестированием,
# чтобы обеспечить "чистый лист" для каждого тестового примера.

#                                                   ВАРИАНТ 1

# main.py:
#
# from fastapi import FastAPI
# from app.auth import router as router_login
# from app.crud_basa import router as router_crud
#
#
# app = FastAPI()
#
# app.include_router(router_login)
# app.include_router(router_crud)
# auth.py:
#
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
#
# from app.models.schemas import User
# from app.dao import UsersDAO
#
#
# router = APIRouter(
#     prefix="/auth",
#     tags=["Auth & Reg"]
# )
#
# security = HTTPBasic()
#
#
# async def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
#     user = await UsersDAO.get_user(name=credentials.username)
#     if not user:
#         raise HTTPException(status_code=404, detail="Not Found")
#     return user
#
#
# @router.post("/login")
# async def login_user(user: User = Depends(authenticate_user)):
#     return user
#
#
# @router.post("/reg")
# async def reg_user(user_data: User):
#     user = await UsersDAO.get_user(name=user_data.name)
#     if user:
#         raise HTTPException(status_code=409)
#     await UsersDAO.add_user(user_data.name, user_data.email)
# crud_basa.py:
#
# from fastapi import APIRouter, HTTPException, Depends
# from app.dao import ProductDAO
# from app.auth import authenticate_user
# from app.models.schemas import Product, User
#
#
# router = APIRouter(
#     prefix="/access",
#     tags=["database"]
# )
#
#
# @router.get("/get_product")
# async def get_product(name: str, user: User = Depends(authenticate_user)) -> list[Product]:
#     product = await ProductDAO.get_product(name=name)
#     if not product:
#         raise HTTPException(status_code=404)
#     return product
#
#
# @router.post("/add_product")
# async def add_product(product: Product, user: User = Depends(authenticate_user)):
#     await ProductDAO.add_product(name=product.name, price=product.price)
#     return {"message": "Done!"}
#
#
# @router.put("/change_product")
# async def change_product(name: str, price: float, user: User = Depends(authenticate_user)):
#     await ProductDAO.update_product(name=name, price=price)
#     return {"message": "Done!"}
#
#
# @router.delete("/delete_product")
# async def delete_product(name: str, user: User = Depends(authenticate_user)):
#     await ProductDAO.delete_product(name=name)
#     return {"message": "Done!"}
# dao.py:
#
# from sqlalchemy import select, insert, delete, update
# from app.config import settings
# from app.database import async_session_maker
# from app.models_sql import Users, Product, TestUser, TestProduct
#
#
# class UsersDAO:
#     model = Users if settings.MODE == "DEV" else TestUser
#
#     @classmethod
#     async def get_user(cls, **filter_data):
#         print(cls.model)
#         async with async_session_maker() as session:
#             query = select("*").select_from(cls.model).filter_by(**filter_data)
#             result = await session.execute(query)
#             return result.mappings().one_or_none()
#
#     @classmethod
#     async def add_user(cls, name, email):
#         async with async_session_maker() as session:
#             query = insert(cls.model).values(name=name, email=email)
#             await session.execute(query)
#             await session.commit()
#
#
# class ProductDAO:
#     model = Product if settings.MODE == "DEV" else TestProduct
#
#     @classmethod
#     async def add_product(cls, name, price):
#         async with async_session_maker() as session:
#             query = insert(cls.model).values(name=name, price=price)
#             await session.execute(query)
#             await session.commit()
#
#     @classmethod
#     async def get_product(cls, **filter_data):
#         async with async_session_maker() as session:
#             query = select("*").select_from(cls.model).filter_by(**filter_data)
#             results = await session.execute(query)
#             return results.mappings().all()
#
#     @classmethod
#     async def update_product(cls, name, price):
#         async with async_session_maker() as session:
#             query = update(cls.model).where(name == cls.model.name).values(price=price)
#             await session.execute(query)
#             await session.commit()
#
#     @classmethod
#     async def delete_product(cls, **filter_data):
#         async with async_session_maker() as session:
#             query = delete(cls.model).filter_by(**filter_data)
#             await session.execute(query)
#             await session.commit()
# database.py:
#
# from sqlalchemy import NullPool
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker
# from app.config import settings
#
# if settings.MODE == "TEST":
#     DATABASE_URL = settings.TEST_DABASE_URL
#     DATABASE_PARAMS = {"poolclass": NullPool}
# else:
#     DATABASE_URL = settings.DATABASE_URL
#     DATABASE_PARAMS = {}
#
# engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
#
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
# class Base(DeclarativeBase):
#     pass
# conftest.py:
#
# import os
#
# os.environ["MODE"] = "TEST"
# config.py:
#
# from typing import Literal
# from pydantic_settings import BaseSettings
# from dotenv import find_dotenv, load_dotenv
#
# load_dotenv(find_dotenv(".env"))
#
# class Settings(BaseSettings):
#     MODE: Literal["DEV", "TEST"]
#
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str
#
#     TEST_DB_HOST: str
#     TEST_DB_PORT: int
#     TEST_DB_USER: str
#     TEST_DB_PASS: str
#     TEST_DB_NAME: str
#
#     @property
#     def DATABASE_URL(self):
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
#
#     @property
#     def TEST_DABASE_URL(self):
#         return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
#
#
#     class ConfigDict:
#         env_file = ".env"
#
#
# settings = Settings()
# test_app.py:
#
# import json
# from fastapi.testclient import TestClient
# from app.main import app
#
#
# client = TestClient(app)
#
#
# class TestMain:
#
#     def test_auth_user(self):
#         test_user_data = {"name": "Itoshi Rin", "email": "rin1109@gmail.com"}
#
#         response = client.post("/auth/login", auth=(test_user_data["name"], test_user_data["email"]))
#
#         assert response.status_code == 200
#
#
#     def test_reg_user(self):
#         test_data = {"name": "Nagi Seishiro", "email": "nagi256@gmail.com"}
#
#         response = client.post("/auth/reg", content=json.dumps(test_data))
#
#         assert response.status_code == 409
#
#
#     def test_add_product(self):
#         test_user_data = {"name": "Itoshi Rin", "email": "rin1109@gmail.com"}
#         test_product = {"name": "Coca-Cola", "price": 28.99}
#
#         response = client.post("/access/add_product", content=json.dumps(test_product), auth=(test_user_data["name"], test_user_data["email"]))
#
#         assert response.status_code == 200
#
#     def test_get_product(self):
#         test_user_data = {"name": "Itoshi Rin", "email": "rin1109@gmail.com"}
#         response = client.get("/access/get_product?name=Coca-Cola", auth=(test_user_data["name"], test_user_data["email"]))
#
#         assert response.status_code == 200
#
#     def test_update_product(self):
#         test_user_data = {"name": "Itoshi Rin", "email": "rin1109@gmail.com"}
#         response = client.put("/access/change_product?name=Coca-Cola&price=34.6", auth=(test_user_data["name"], test_user_data["email"]))
#
#         assert response.status_code == 200
#
#     def test_delete_product(self):
#         test_user_data = {"name": "Itoshi Rin", "email": "rin1109@gmail.com"}
#         response = client.delete("/access/delete_product?name=Coca-Cola", auth=(test_user_data["name"], test_user_data["email"]))
#
#         assert response.status_code == 200
# .env:
#
# MODE="DEV"
#
# DB_HOST=*****
# DB_PORT=*****
# DB_USER=*****
# DB_PASS=*****
# DB_NAME=*****
#
# TEST_DB_HOST=*****
# TEST_DB_PORT=*****
# TEST_DB_USER=*****
# TEST_DB_PASS=*****
# TEST_DB_NAME=*****