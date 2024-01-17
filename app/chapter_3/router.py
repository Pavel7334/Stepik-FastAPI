from typing import Annotated

from fastapi import APIRouter, Header, HTTPException

router = APIRouter(
    prefix="/tasks",
    tags=["Chapter_3:"]
)

# from fastapi.responses import FileResponse
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}
#
#
# @app.get("/custom")
# def read_custom_message():
#     return {"message": "This is a custom message!"}
#
# # @app.get("/")
# # async def root():
# #     return FileResponse('index.html')
#
# # @app.post("/calculate")
# # async def root(num1: int, num2: int):
# # #     return {"result": num1 + num2}

# from typing import Optional
# from fastapi import FastAPI
#
# from models import User
#
# app = FastAPI()
#
# my_user = {
#
#     "name": "John Doe",
#
#     "id": 1
#
# }
#
#
# @app.post("/users")
# async def get_user_data():
#     '''тут мы можем с переменной user, которая в себе содержит объект класса User с соответствующими полями
#     (и указанными типами), делать любую логику
#     - например, мы можем сохранить информацию в базу данных
#     - или передать их в другую функцию
#     - или другое'''
#     # print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}')
#     # # тут мы просто выведем полученные данные на экран в отформатированном варианте
#
#     return my_user
#     # или можем вернуть обратно полученные данные, как символ того, что данные получили, или другая логика на ваш вкус


# from fastapi import FastAPI
#
# from models import FeedBack
#
# app = FastAPI()
#
# # Пример пользовательских данных (для демонстрационных целей)
# fake_users = {
#     1: {"username": "john_doe", "email": "john@example.com"},
#     2: {"username": "jane_smith", "email": "jane@example.com"},
# }

# # Конечная точка для получения информации о пользователе по ID
# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     if user_id in fake_users:
#         return fake_users[user_id]
#     return {"error": "User not found"}


# @app.get("/users/")                                   # ЛИМИТ ДЛЯ ВЫВОДА ЮЗЕРОВ
# def read_users(limit: int = 10):
#     return dict(list(fake_users.items())[:limit])

# fake_feedback = {}
# counter = 0
#
#
# @app.post("/feedback")
# async def add_feedback(feedback: Feedback):
#     global counter
#     counter += 1
#     return {f"Ваш отзыв '{feedback.message}'": f"Спасибо, {feedback.name}!"}


# lst = []
#
#
# @app.post("/feedback")
# async def send_feedback(feedback: FeedBack):
#     lst.append({"name": feedback.name, "comments": feedback.message})
#     return f"Feedback received. Thank you, {feedback.name}!"
#
#
# @app.get("/comments")
# async def show_feedback():
#     return lst


#                       МОДЕЛИ ЗАПРОСОВ И ОТВЕТОВ

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#
#
# @app.post("/items/")
# async def create_item(item: Item) -> Item: # тут мы передали в наш обработчик Pydantic модель, чтобы она проверяла все
#     # апросы на соответствие этой модели (все поля и типы данных в них должны соответствовать модели
#     return item
#
#
# @app.get("/items/")
# async def read_items() -> list[Item]: # тут мы не принимаем никаких данных, но указываем, что возвращаться будет список,
#     # содержащий в себе Pydantic модели
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]


#                           ОБРАБОТКА ЗАГРУЗКИ ФАЙЛОВ

# from typing import Annotated # про это будет чуть позднее в курсе
#
# from fastapi import FastAPI, File, UploadFile
#
# app = FastAPI()
#
#
# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}


#                           Обработка параметров запроса

# from fastapi import FastAPI
#
# app = FastAPI()
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


#                           Тело запроса и параметры пути

# from typing import Union
#
# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
#
# app = FastAPI()
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr
# from typing import Union
#
# app = FastAPI()
#
# fake_users_db = []
#
#
# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     age: Union[int, None] = None
#     is_subscribed: Union[bool, None] = None
#
#
# @app.post('/create_user', response_model=UserCreate)
# async def create_user(user_data: UserCreate):
#     fake_users_db.append(user_data)
#     return user_data


#                                   Обработка запросов и их проверка

# from typing import Optional
#
# sample_product_1 = {
#     "product_id": 123,
#     "name": "Smartphone",
#     "category": "Electronics",
#     "price": 599.99
# }
#
# sample_product_2 = {
#     "product_id": 456,
#     "name": "Phone Case",
#     "category": "Accessories",
#     "price": 19.99
# }
#
# sample_product_3 = {
#     "product_id": 789,
#     "name": "Iphone",
#     "category": "Electronics",
#     "price": 1299.99
# }
#
# sample_product_4 = {
#     "product_id": 101,
#     "name": "Headphones",
#     "category": "Accessories",
#     "price": 99.99
# }
#
# sample_product_5 = {
#     "product_id": 202,
#     "name": "Smartwatch",
#     "category": "Electronics",
#     "price": 299.99
# }
#
# sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]
#
#
# @router.get('/product/{product_id}')
# async def get_product(product_id: int):
#     result = [item for item in sample_products if product_id == item['product_id']]
#     if result:
#         return result
#     return {'message': 'Product not found'}
#
#
# @router.get('/products/search')
# async def product_search(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
#     return [i for i in sample_products if keyword in i['name'] and (not category or category in i['category'])][:limit]


#                                                   3.2

#                       Дополнительные типы данных, асинхронность и параметры Cookie


# Фоновые задачи в FastAPI

"""FastAPI также поддерживает фоновые задачи, которые представляют собой функции, выполняемые после отправки ответа 
клиенту. Фоновые задачи полезны для обработки задач, которые не должны блокировать основной цикл запроса-ответа, таких 
как отправка электронных писем, обновление аналитики или выполнение дополнительной неблокирующей обработки.
Чтобы использовать фоновые задачи в FastAPI, вы можете определить функцию фоновой задачи (с использованием класса 
BackgroundTasks) и включить ее в качестве параметра в обработчик маршрута."""

# from fastapi import BackgroundTasks
#
#
# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)
#
#
# @router.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}


# Параметры Cookie

"""Вы можете задать параметры Cookie таким же способом, как Query и Path параметры.

FastAPI поддерживает три типа файлов cookie:

а) Обычные файлы cookie: Это стандартные файлы cookie, которые хранятся на стороне клиента и отправляются обратно на 

сервер при каждом запросе. Обычные файлы cookie широко используются для различных целей, таких как управление сеансами 

и пользовательскими настройками.

б) Защищенные файлы cookie: Защищенные файлы cookie - это зашифрованные файлы cookie, которые обеспечивают 

дополнительный уровень безопасности. Под защищенными куками мы имеем ввиду куки, в которых установлен флаг Secure, 

который говорит браузеру, что эти куки можно передавать только по SSL-соединению.

Примечание: рекомендуем прочитать про XSS-атаки, и дополнительную защиту куков при помощи установки флага HttpOnly, 

чтобы гарантировать, что данные файлов cookie остаются конфиденциальными и не могут быть использованы злоумышленниками 

с использованием внедрения вредоносного Javascript'а на сайтах.

c) Подписанные файлы cookie: Подписанные файлы cookie - это файлы cookie, которые содержат подпись для проверки их 

подлинности. Они гарантируют, что данные cookie-файлов не были изменены клиентом с тех пор, как они были установлены 

сервером.

Для доступа к кукам сначала импортируйте класс Cookie из fastapi. Затем объявляйте параметры cookie, используя ту же 

структуру, что и с Path и Query."""

# from fastapi import Cookie, FastAPI
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(ads_id: str | None = Cookie(default=None)):
#     return {"ads_id": ads_id}


# Доступ к файлам cookie

"""FastAPI упрощает доступ к файлам cookie в запросе. Вы можете извлекать данные cookie и работать с ними в 

своих обработчиках маршрутов точно так же, как с любыми другими данными.

Для получения куки на сервере применяется класс fastapi.Cookie"""

# from fastapi import FastAPI, Cookie
#
# app = FastAPI()
#
#
# @app.get("/")
# def root(last_visit=Cookie()):
#     return {"last visit": last_visit}


# Установка файлов cookie Установка файлов cookie

"""В FastAPI вы можете установить файлы cookie в ответе, используя метод `set_cookie` в параметре Response. Этот метод 

позволяет вам определить имя файла cookie, значение и дополнительные параметры, такие как домен, путь, срок действия и 

параметры безопасности."""

# from fastapi import FastAPI, Response
# from datetime import datetime
#
# # app = FastAPI()
#
#
# @router.get("/")
# def root(response: Response):
#     now = datetime.now()  # получаем текущую дату и время
#     response.set_cookie(key="last_visit", value=now)
#     return {"message": "куки установлены"}


# Прочие возможности при работе с cookie

"""Вы можете указать время истечения срока действия файла cookie, используя параметр "expires", или установить 

максимальный возраст, используя параметр "max_age". Это помогает контролировать срок службы файлов cookie и 

эффективно управлять данными сеанса.

FastAPI предоставляет простой способ удалить файлы cookie, установив время их истечения в прошлом. Это дает указание 

клиенту удалить файл cookie из своего хранилища."""

"""Также у класса Response есть метод delete_cookie, который принимает в качестве аргумента строку (наименование куки) 

и удаляет ее на стороне клиента.


Для примера:

@router.post("/logout", status_code=204)
async def logout_user(response: Response):
    response.delete_cookie("example_access_token")
    
Под капотом, этот метод вызывает метод set_cookie и устанавливает атрибутам max_age и expires значение 0.

На этом данный урок заканчивается. Давайте продолжим наше путешествие по созданию мощных и безопасных API-интерфейсов с 

помощью FastAPI! """

# Задача на программирование

# from fastapi import Cookie, Response
# from app.chapter_3.models import User
#
# # имитируем хранилище юзеров
# sample_user: dict = {"username": "user123", "password": "password123"}  # создали тестового юзера, якобы он уже
# # зарегистрирован у нас
# fake_db: list[User] = [User(**sample_user)]  # имитируем базу данных
#
# # имитируем хранилище сессий
# sessions: dict = {}  # это можно хранить в кэше, например в Redis
#
#
# @router.post('/login')
# async def login(user: User, response: Response):
#     for person in fake_db:  # перебрали юзеров в нашем примере базы данных
#         if person.username == user.username and person.password == user.password:  # сверили логин и пароль
#             session_token = "abc123xyz456"  # тут можно использовать модуль uuid (в продакшене), или модуль random
#             # (для выполнения задания), или самому написать рандомное значение куки, т.к. это пример тестовый
#             sessions[session_token] = user  # сохранили у себя в словаре сессию, где токен - это ключ, а значение -
#             # объект юзера
#             response.set_cookie(key="session_token", value=session_token, httponly=True)  # тут установили куки с
#             # защищенным флагом httponly - недоступны для вредоносного JS; флаг secure означает, что куки идут только
#             # по HTTPS
#             return {"message": "куки установлены"}
#     return {"message": "Invalid username or password"}  # тут можно вернуть что хотите, в ТЗ не конкретезировалось,
#     # что делать, если логин/пароль неправильные
#
#
# @router.get('/user')
# async def user_info(session_token=Cookie()):
#     user = sessions.get(
#         session_token)  # ищем в сессиях был ли такой токен создан, и если был, то возвращаем связанного
#     # с ним юзера
#     if user:
#         return user.dict()  # у pydantic моделей есть метод dict(), который делает словарь из модели. Можно сразу
#         # хранить словарь в сессии, не суть. Для Pydantic версии > 2 метод переименован в model_dump()
#     return {"message": "Unauthorized"}


#                                           3.3

#                               Работа с заголовками запросов

#                                   Заголовки запросов
# """HTTP-заголовки - это метаданные, которые сопровождают HTTP-запрос или ответ. FastAPI позволяет вам получать
#
# доступ к заголовкам запросов и работать с ними для извлечения важной информации, такой как токены аутентификации,
#
# юзер-агенты и типы контента.
#
# FastAPI позволяет вам получать доступ к заголовкам запросов (headers) в рамках ваших функций маршрутизации.
#
# Вы можете использовать заголовки для предоставления дополнительной информации или данных авторизации вашему API."""
#
# from typing import Annotated
#
# from fastapi import FastAPI, Header
#
# app = FastAPI()
#
#
# @router.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header()] = None):
#     return {"User-Agent": user_agent}
#
#
# """Разберём эту строчку: user_agent: Annotated[str | None, Header()] = None:
#
# user_agent - это имя заголовка, который мы ищем;
#
# при помощи Annotated мы задаём тип данных в заголовке (строка или None), соответственно другие типы не пройдут
# валидацию;
# также мы аннотируем формат тем, что указываем, что ожидаем именно заголовок (при помощи нашего класса Header) - то есть
#
# с помощью Annotated можно аннотировать переменную чем-то другим, кроме ее типа (например, строкой документации, чтобы
#
# какой-то гипотетический инструмент мог использовать ее для автоматического создания документации) или в нашем
#
# случае - классом, то есть мы говорим что тип - это строка или None, с одной стороны, но и заголовок - с другой;
#
# в дополнение класс Header переводит наш snake_case у user_agent к формату заголовков ("User-Agent") - искать
#
# будет именно его;
#
# и последнее - мы задаём значение заголовка по-умолчанию (=None ), и если заголовок не поступит в запросе, то
#
# внутри функции переменная user_agent будет равна None...мы можем задать здесь любое другое значение по умолчанию,
#
# если захотим."""


#                               Автоматическое преобразование

# """Класс заголовок (Header) обладает небольшой дополнительной функциональностью в дополнение к тому, что
#
# предоставляют Path, Query и Cookie.
#
# Большинство стандартных заголовков разделены символом "дефис", также известным как "символ минуса" (-).
#
# Но переменная, подобная user-agent, недопустима в Python.
#
# Таким образом, по умолчанию Header преобразует символы имен параметров из символа подчеркивания (_) в дефис (-) для
#
# извлечения и документирования заголовков.
#
# Кроме того, HTTP-заголовки не чувствительны к регистру, поэтому вы можете объявить их в стандартном стиле Python
#
# (также известном как "snake_case").
#
# Итак, вы можете использовать user_agent, как обычно, в коде Python, вместо того, чтобы использовать заглавные буквы
#
# как User_Agent или что-то подобное.
#
# Если по какой-либо причине вам необходимо отключить автоматическое преобразование подчеркиваний в дефисы, установите
#
# параметр convert_underscores заголовка значение False."""

#                                       Повторяющиеся заголовки

# """В FastAPI возможно получение повторяющихся заголовков. Это означает, что один и тот же заголовок содержит несколько
#
# значений.
#
# Вы можете определить эти случаи, используя список в объявлении типа. Вы получите все значения из дублирующегося
#
# заголовка в виде списка Python.
#
# Например, чтобы объявить заголовок X-Token, который может появляться более одного раза, вы можете написать:"""
#
# from typing import Annotated
#
# from fastapi import FastAPI, Header
#
# app = FastAPI()
#
#
# @router.get("/items/")
# async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
#     return {"X-Token values": x_token}
# Если вы взаимодействуете с этой операцией path, отправляя два HTTP-заголовка, таких как:

# X-Token: foo
# X-Token: bar
# Ответ был бы таким:

# """"{
#     "X-Token values": [
#         "bar",
#         "foo"
#     ]
# }"""


#                                           Доступ к заголовкам запросов

# """Для получения заголовков запроса применяется класс fastapi.Header. Например, получим заголовок User-Agent:
#
# from fastapi import FastAPI, Header
#
# app = FastAPI()
#
#
# @app.get("/")
# def root(user_agent: str = Header()):
#     return {"User-Agent": user_agent}
# Для отправки заголовка в конструктор класса Response или его наследников параметру headers передается словарь, где
# ключи представляют названия заголовков:
#
# from fastapi import FastAPI, Response
#
# app = FastAPI()
#
# @app.get("/")
# def root():
#     data = "Hello from here"
#     return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123459"})
# Также можно задать заголовки с помощью атрибута headers, который есть у класса Response и его наследников. Данный
# атрибут фактически представляет словарь, где ключи - названия заголовков:
#
# from fastapi import FastAPI, Response
#
# app = FastAPI()
#
# @app.get("/")
# def root(response: Response):
#     response.headers["Secret-Code"] = "123459"
#     return {"message": "Hello from my api"}
# Вот и все для этого урока! Теперь у вас есть полное представление об обработке заголовков запросов  в FastAPI."""

#                                       Задача на программирование

# @router.get('/headers')
# async def headers(
#         user_agent: Annotated[str | None, Header()] = None,
#         accept_language: Annotated[str | None, Header()] = None):
#     if not user_agent or not accept_language:
#         raise HTTPException(status_code=400, detail='Необходимые заголовки отсутствуют')
#     return {'User-Agent': user_agent, 'Accept-Language': accept_language}


