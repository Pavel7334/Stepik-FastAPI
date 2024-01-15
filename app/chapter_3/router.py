from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Глава chapter_3:"
          "Часть chapter_3.1"]
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

from typing import Optional

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@router.get('/product/{product_id}')
async def get_product(product_id: int):
    result = [item for item in sample_products if product_id == item['product_id']]
    if result:
        return result
    return {'message': 'Product not found'}


@router.get('/products/search')
async def product_search(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
    return [i for i in sample_products if keyword in i['name'] and (not category or category in i['category'])][:limit]