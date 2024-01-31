from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["Chapter_6:"]
)

#                                                     6.1

#                                             Важность обработки ошибок

# Обработка ошибок является важнейшим аспектом создания надежных веб-приложений. Это включает в себя предвидение
# потенциальных ошибок или исключений, которые могут возникнуть во время выполнения приложения, и корректную обработку
# их. В этом уроке мы сосредоточимся на пользовательской (кастомной) обработке ошибок в FastAPI, чтобы обеспечить
# информативные и удобные для пользователя ответы на ошибки.

#                                         Ответы на ошибки по умолчанию в FastAPI

# FastAPI автоматически генерирует ответы об ошибках для распространенных кодов состояния HTTP, таких как 404
# (Not found) или 500 (internal server error). Хотя эти ответы по умолчанию полезны, пользовательская обработка ошибок
# позволяет нам адаптировать ответы на ошибки в соответствии с требованиями нашего приложения.

#                                       Создание пользовательских классов исключений

# В FastAPI мы можем создавать пользовательские классы исключений, которые наследуются от встроенного класса
# `HttpException`. Эти пользовательские классы исключений позволяют нам определять конкретные сообщения об ошибках,
# коды состояния и дополнительные сведения для включения в ответ на ошибку.
#
# from fastapi import FastAPI, HTTPException
#
# app = FastAPI()
#
#
# # класс кастомного исключения для ошибок
# class CustomException(HTTPException):
#     def __init__(self, detail: str, status_code: int = 400):
#         super().__init__(status_code=status_code, detail=detail)
#
#
# # пример маршрута, который райзит (выбрасывает) кастомное исключение
# @app.get("/items/{item_id}/")
# async def read_item(item_id: int):
#     if item_id == 42:
#         raise CustomException(detail="Item not found", status_code=404)
#     return {"item_id": item_id}
# В приведенном выше примере мы создали пользовательский класс исключений `CustomException`, который наследуется от
# `HttpException`. Класс `CustomException` принимает два параметра: `detail` (сообщение об ошибке) и `status_code`
# (код состояния HTTP). Мы вызываем метод `__init__` родительского класса `HttpException` с предоставленными
# аргументами `detail` и `status_code`.
#
# В маршруте `read_item` мы проверяем, равен ли `item_id` 42. Если это так, мы создаем наше пользовательское
# исключение с сообщением об ошибке "Элемент не найден" и кодом состояния 404 (Not found). В противном случае мы
# возвращаем словарь с `item_id`.
#
# Использование пользовательских классов исключений, подобных этому, позволяет вам создавать более значимые и
# конкретные ответы на ошибки для вашего API. Вы можете адаптировать сообщения об ошибках и коды состояния в
# соответствии с требованиями вашего приложения и предоставлять клиентам четкую информацию при возникновении ошибки.

#                                 Регистрация пользовательских обработчиков исключений

# После создания пользовательских классов исключений мы можем зарегистрировать обработчики исключений для захвата и
# обработки определенных типов исключений. FastAPI предоставляет декоратор `@app.exception_handler` для связывания
# классов исключений с их соответствующими обработчиками.
#
# Давайте расширим предыдущий код для регистрации Error handler'а (обработчика исключений):
#
# from fastapi import FastAPI, HTTPException, Request
# from fastapi.responses import JSONResponse
#
# app = FastAPI()
#
#
# # не изменяли
# class CustomException(HTTPException):
#     def __init__(self, detail: str, status_code: int = 400):
#         super().__init__(status_code=status_code, detail=detail)
#
#
# # Обработчик ошибок (error handler) для класса CustomException
# @app.exception_handler(CustomException)
# async def custom_exception_handler(request: Request, exc: CustomException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"error": exc.detail}
#     )
#
#
# # не изменяли
# @app.get("/items/{item_id}/")
# async def read_item(item_id: int):
#     if item_id == 42:
#         raise CustomException(detail="Item not found", status_code=404)
#     return {"item_id": item_id}
# В обновленном коде мы добавили пользовательский обработчик ошибок с именем `custom_exception_handler` для класса
# `CustomException`, используя декоратор `app.exception_handler()`. Эта функция принимает два параметра: `request`
# (текущий объект запроса) и `exc` (экземпляр вызванного исключения).
#
# Функция `custom_exception_handler` возвращает `JsonResponse` с соответствующим кодом состояния HTTP и телом JSON,
# содержащим поле `error` с сообщением `detail` пользовательского исключения.
#
# Теперь всякий раз, когда в приложении возникает `CustomException` (как мы делаем в маршруте `/items/{item_id}/`),
# будет вызван пользовательский обработчик ошибок, и пользовательский ответ об ошибке будет возвращен клиенту.
#
# Такой подход позволяет вам обрабатывать конкретные исключения с помощью настраиваемых ответов, обеспечивая лучший
# контроль и согласованность при обработке ошибок во всем вашем приложении FastAPI.

#                                               Логгирование ошибок

# Логгирование ошибок - важная практика при разработке приложений. FastAPI позволяет нам регистрировать ошибки и
# соответствующую информацию, чтобы помочь в отладке и устранении неполадок. Для этих целей обычно используется
# библиотека logging. Продвинутые инструменты для работы с логами будут предложены позднее в курсе, чтобы вы знали
# об их наличии и изучили, при необходимости.

#                                       Отправка пользовательских сообщений об ошибках

# С помощью пользовательских обработчиков исключений мы можем настроить ответы на ошибки, возвращаемые нашим
# приложением FastAPI. Это позволяет нам предоставлять пользователям значимые сообщения об ошибках и полезную
# информацию при возникновении проблем. В коде в приведённом примере мы это и сделали. Вы можете настроить
# возвращаемых ответ в соответствии с вашими потребностями.

#                                           Глобальные обработчики исключений

# В дополнение к регистрации обработчиков исключений для конкретных исключений, FastAPI также позволяет нам определять
# глобальные обработчики исключений, которые перехватывают все необработанные исключения. Эти глобальные обработчики
# могут обеспечить резервный ответ на непредвиденные ошибки, чтобы предотвратить утечку конфиденциальной информации
# пользователям.
#
# Давайте добавим глобальный обработчик исключений:
#
# from fastapi import FastAPI, HTTPException, Request
# from fastapi.responses import JSONResponse
#
# app = FastAPI()
#
#
# # не изменяли
# class CustomException(HTTPException):
#     def __init__(self, detail: str, status_code: int = 400):
#         super().__init__(status_code=status_code, detail=detail)
#
#
# # не изменяли
# @app.exception_handler(CustomException)
# async def custom_exception_handler(request: Request, exc: CustomException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"error": exc.detail}
#     )
#
#
# # Обработчик глобальных исключений, который "ловит" все необработанные исключения
# @app.exception_handler(Exception)
# async def global_exception_handler(request: Request, exc: Exception):
#     return JSONResponse(
#         status_code=500,
#         content={"error": "Internal server error"}
#     )
#
#
# # добавили непредусмотренное исключение
# @app.get("/items/{item_id}/")
# async def read_item(item_id: int):
#     # симулируем непредусмотренное исключение
#     result = 1 / 0
#     return {"item_id": item_id}
# В приведенном выше коде у нас есть два обработчика исключений. Первый, `custom_exception_handler`, специфичен для
# класса `CustomException`, как показано в предыдущем примере.
#
# Второй обработчик исключений, `global_exception_handler`, не указывает какой-либо конкретный тип исключения, что
# делает его глобальным обработчиком исключений. Этот обработчик будет перехватывать все необработанные исключения в
# приложении FastAPI.
#
# В маршруте `/items/{item_id}/` мы имитируем необработанное исключение, разделив `1` на `0`. Поскольку это явно не
# перехватывается каким-либо конкретным обработчиком исключений, оно будет перехвачено глобальным обработчиком
# исключений.
#
# Глобальный обработчик исключений возвращает общий ответ об ошибке с кодом состояния `500` (внутренняя ошибка сервера)
# и сообщением, указывающим на то, что произошла внутренняя ошибка сервера. Это предотвращает утечку конфиденциальной
# информации к пользователям в случае непредвиденных ошибок.
#
# Определив глобальный обработчик исключений, вы можете корректно обрабатывать неожиданные исключения и предоставлять
# согласованные ответы на ошибки во всем вашем приложении FastAPI.


#                                            Модели реагирования на ошибки

# FastAPI позволяет нам определять модели реагирования на ошибки, используя модели Pydantic. Определяя структуру
# ответов об ошибках, мы можем обеспечить согласованное форматирование и данные в наших сообщениях об ошибках.
#
# Тут пример будет достаточно лаконичным:
#
# from pydantic import BaseModel
#
# # Pydantic модель ответов на ошибки
# class ErrorResponse(BaseModel):
#     error_code: int
#     error_message: str
#     error_details: str = None
# В данном примере мы наследовались от стандартного Pydantic класса BaseModel, определив, что наш кастомной класс
# будет содержать 3 поля: код ошибки, сообщение и детали. Вы можете настроить его любым необходимым образом, например
# добавив категорирование, тип или любую другую релевантную информацию.

#                                                        ЗАДАЧА

# Для этой задачи программирования вам необходимо реализовать пользовательскую обработку ошибок в приложении FastAPI.
# Ваше приложение должно включать пользовательские классы исключений, обработчики исключений и модели реагирования на
# ошибки.
#
# Требования:
#
# 1. Создайте приложение FastAPI и настройте пользовательские классы исключений по крайней мере для двух конкретных
# исключений (например, `CustomExceptionA` и `CustomExceptionB`). Каждое пользовательское исключение должно иметь
# уникальный код состояния и пользовательское сообщение об ошибке.
#
# 2. Зарегистрируйте пользовательские обработчики исключений для двух пользовательских исключений. Обработчики
# сключений должны возвращать ответы об ошибках с соответствующими кодами состояния и сообщениями об ошибках.
#
# 3. Определите модели реагирования на ошибки, используя модели Pydantic, чтобы обеспечить согласованное
# форматирование ответов на ошибки во всем приложении.
#
# 4. Реализуйте по крайней мере две конечные точки API, которые вызывают пользовательские исключения в определенных
# сценариях. Например, одна конечная точка может вызвать `CustomExceptionA`, когда не выполняется определенное
# условие, а другая конечная точка может вызвать `CustomExceptionB`, когда ресурс не найден.
#
# 5. Протестируйте свою пользовательскую обработку ошибок, отправив запросы к конечным точкам API, которые вызывают
# пользовательские исключения. Убедитесь, что ответы об ошибках содержат правильные коды состояния и сообщения об
# ошибках.
#
# Примечание: Для этой задачи вы можете использовать простые инструкции печати для регистрации ошибок. В реальном
# сценарии вы обычно использовали бы библиотеку ведения журнала для эффективной обработки регистрации ошибок.

# Модель:
#
# class ErrorResponse(BaseModel):
#     status_code: int
#     detail: str
#
#
# Все остальное:
#
# class CustomExceptionA(HTTPException):
#     def __init__(self, detail: str, status_code: int = 500):
#         super().__init__(detail=detail, status_code=status_code)
#
#
# class CustomExceptionB(HTTPException):
#     def __init__(self, detail: str, status_code: int = 400):
#         super().__init__(detail=detail, status_code=status_code)
#
#
# @app.exception_handler(CustomExceptionA)
# async def custom_exception_handler_a(request: Request, exc: ErrorResponse):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail}
#     )
#
#
# @app.exception_handler(CustomExceptionB)
# async def custom_exception_handler_b(request: Request, exc: ErrorResponse):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail}
#     )
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 5:
#         raise CustomExceptionA(detail="Server very error", status_code=500)
#     return {"item_id": item_id}
#
#
# @app.get("/primer/{primer_id}")
# async def read_item(primer_id: int):
#     if primer_id == 7:
#         raise CustomExceptionB(detail="Not found", status_code=404)
#     return {"primer_id": primer_id}


#                                                       6.2

#                                       Введение в ошибки проверки (валидации) данных

# Ошибки проверки (валидации) возникают, когда данные, отправленные в веб-приложение, не соответствуют указанным
# правилам или требованиям проверки. FastAPI предоставляет мощные инструменты для эффективной обработки ошибок
# проверки, гарантируя, что приложение обрабатывает только достоверные данные. В этом уроке мы рассмотрим, как
# обрабатывать ошибки проверки (валидации) в приложениях FastAPI

#                                              Проверка данных запроса

# FastAPI использует мощные возможности проверки данных Pydantic для проверки входящих данных запроса. Определяя
# модели Pydantic или указывая тип ожидаемых (принимаемых) данных для тел запросов, параметров запроса, параметров
# пути и заголовков, мы можем автоматически проверять данные на соответствие правилам указанной модели
# (указанным типам).

#                                              Обработка ошибок проверки

# Когда данные не проходят проверку, FastAPI автоматически вызывает `HttpException` с кодом состояния объекта 422
# Unprocessable entity. Это исключение содержит подробную информацию об ошибках проверки, что облегчает определение
# причины несоответствия.

#                                           Настройка ответов на ошибки проверки

# FastAPI позволяет нам настраивать ответы на ошибки проверки, чтобы предоставлять пользователям более содержательную
# обратную связь. Мы можем создать пользовательские обработчики ошибок проверки с помощью
# декоратора `@app.exception_handler` и настроить содержимое ответа и код состояния.

#                                          Обработка ошибок в теле запроса FastAPI

# FastAPI также позволяет нам контролировать, как обрабатываются ошибки синтаксического анализа тела запроса. По
# умолчанию ошибки синтаксического анализа тела запроса возвращают код состояния объекта 422 Unprocessable entity.
# Однако мы можем переопределить это поведение и настроить ответ так, чтобы он лучше соответствовал потребностям
# нашего приложения.
#
# Пример модели для проверки тела запроса:
#
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
# Давайте расширим этот код, добавив пользовательское сообщение об ошибке:
#
# from typing import Union
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
#
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
# app = FastAPI()
#
# @app.post("/items/")
# async def create_item(item: Item):
#     try:
#         # тут добавили дополнительную проверку
#         if item.price < 0:
#             raise ValueError("Price must be non-negative")
#
#         # это вернётся в случае успеха
#         return {"message": "Item created successfully", "item": item}
#     except ValueError as ve:
#         # обрабатываем нашу ошибку валидации и пробрасываем ошибку выше с кастомным ответом
#         raise HTTPException(status_code=400, detail=str(ve))
# С использованием декоратора @app.exception_handler это могло бы выглядеть так:
#
# from typing import Union
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
#
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
# app = FastAPI()
#
# @app.exception_handler(ValueError)  # кастомный хэндлер для ValueError
# async def value_error_handler(request, exc):
#     return JSONResponse(status_code=400, content={"error": str(exc)})
#
# @app.post("/items/")
# async def create_item(item: Item):
#     try:
#         if item.price < 0:
#             raise ValueError("Price must be non-negative")
#
#         # вернём при успехе
#         return {"message": "Item created successfully", "item": item}
#     except ValueError as ve:
#         # выбрасываем ValueError чтобы сработал кастомный обработчик нашего исключения
#         raise ve
# Или продвинутый пример работы с ошибками валидации:
#
# from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
#
# app = FastAPI()
#
# # кастомный обработчик исключения для всех HTTPException
# async def custom_http_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"error": str(exc)},
#     )
#
# # кастомный обработчик исключения для RequestValidationError (Pydantic validation errors - 422 Unprocessable Entity)
# async def custom_request_validation_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=422,
#         content={"message": "Custom Request Validation Error", "errors": exc.errors()},
#     )
#
# # тут показываем альтернативный декораторам способ регистрации хэндлеров
# app.add_exception_handler(HTTPException, custom_http_exception_handler)
# app.add_exception_handler(RequestValidationError, custom_request_validation_exception_handler)
#
# class Item(BaseModel):
#     name: str
#     price: float
#
# @app.post("/items/")
# async def create_item(item: Item):
#     if item.price < 0:
#         raise HTTPException(status_code=400, detail="Price must be non-negative")
#     return {"message": "Item created successfully", "item": item}
# Также Pydantic позволяет расширить валидацию, добавив собственные валидаторы, например так:
#
# from typing import Union
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, validator
#
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
#     @validator("price")
#     @classmethod
#     def validate_price(cls, value):
#         if value < 0:
#             raise ValueError("Price must be non-negative")
#         return value
#
# app = FastAPI()
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return {"message": "Item created successfully", "item": item}
#
# Пользовательские валидаторы могут быть очень мощными и могут помочь вам создавать модели данных, адаптированные к
# вашим конкретным потребностям. Только будьте аккуратны с регулярными выражениями :)

#               Проверка с использованием параметров запроса, параметров пути и параметров заголовков

# FastAPI расширяет свои возможности проверки также на параметры запроса, пути и заголовков (как мы указывали ранее).
# Определяя модели Pydantic для этих параметров (или указывая в параметрах функции явно ожидаемый тип данных), мы
# можем проверять и автоматически преобразовывать данные до того, как они достигнут наших функций конечной точки, а
# потом уже обрабатывать по аналогии с предыдущим примером.
#
# Пример валидации Query-параметров:
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: str | None = None): # валидируем тут и задаём значение по-умолчанию
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
# Пример валидации Path-параметров:
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int): # задаём тип тут
#     return {"item_id": item_id}
# Пример валидации Header-параметров:
#
# from typing import Annotated
#
# from fastapi import FastAPI, Header
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header()] = None): # задаём тип тут
#     return {"User-Agent": user_agent}

#                                             Задача на программирование

# Для этой задачи программирования вам необходимо реализовать проверку данных запроса и пользовательскую обработку
# ошибок проверки в приложении FastAPI.
#
# Требования:
#
# 1. Создайте приложение FastAPI по крайней мере с одной конечной точкой, которая принимает полезную нагрузку JSON,
# представляющую данные пользователя (например, "name", "age", "e-mail" и др. согласно примеру ниже, либо можете
# использовать свой пример).
#
# 2. Определите модель Pydantic для пользовательских данных, чтобы выполнить проверку входящей полезной нагрузки JSON.
#
# class User(BaseModel):
#     username: str
#     age: conint(gt=18)
#     email: EmailStr
#     password: constr(min_length=8, max_length=16)
#     phone: Optional[str] = 'Unknown'
# Немного прокомментируем, чтобы вы знали больше, чем мы рассказывали ранее:
#
# В username - проверка на строку, ничего необычного;
#
# conint - это int с ограничениями (от "add constraints");
#
# gt=18 - greater than - больше чем; прочитайте про другие сокращения в FastAPI;
#
# EmailStr - проверяет, удовлетворяет ли строка требованиям к емейлу (либо можете написать сами регулярку);
#
# constr - аналогично предыдущему, но строка с ограничениями (ограничения по длине - заданы минимальная и
# максимальная длины);
#
# Optional[str] - переменная имеет тип str, но это является «необязательным». И также указали значение по умолчанию.
#
# 3. Реализуйте пользовательскую обработку ошибок проверки с помощью декоратора `@app.exception_handler`, чтобы
# предоставлять информативные ответы об ошибках при сбоях проверки.
#
# 4. Протестируйте обработку ошибок пользовательской проверки, отправив запросы с неверными пользовательскими данными
# в конечную точку и убедившись, что ответы об ошибках содержат соответствующие коды состояния и сообщения об ошибках.
#
# Примечание: Вы можете использовать `fastapi.testclient.TestClient` для выполнения тестовых запросов к вашему
# приложению FastAPI и проверки ответов (про него мы расскажем в следующем блоке).

# from __future__ import annotations
# from typing import Any, Optional
# from fastapi import FastAPI, HTTPException, status
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, conint, EmailStr, constr, validator
#
#
# class User(BaseModel):
#     username: str
#     age: conint(gt=18)
#     email: EmailStr
#     password: constr(min_length=8, max_length=16)
#     phone: Optional[str] = 'Unknown'
#
#     @validator('age')
#     @classmethod
#     def validate_age(cls: User, value: int) -> User:
#         if value > 110:
#             raise ValueError('User age must be lower than 110')
#         return value
#
#
# app = FastAPI()
#
# @app.exception_handler(ValueError)
# async def value_error_handler(request, exc):
#     print(f"value_error_handler: ")
#     return JSONResponse(
#         status_code=422,
#         content={"message": "Custom Request Validation Error", "errors": exc.errors()},
#     )
#
# @app.post('/user')
# async def post_user(user: User) -> User:
#     if user.age > 100:
#         raise HTTPException(detail='User too old', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
#     return user


#                                                  6.3

#                                               Дополнительные возможности

# Как вы поняли, настраиваемые ответы на ошибки играют важную роль в улучшении пользовательского интерфейса вашего
# приложения FastAPI. В то время как FastAPI предоставляет ответы на ошибки по умолчанию, создание пользовательских
# сообщений об ошибках позволяет предоставлять более удобную для пользователя и информативную обратную связь при
# возникновении исключений. В данном уроке мы пробежимся по некоторым дополнительным возможностям в работе с ошибками,
# чтобы вы при необходимости могли их отдельно изучить.

#                                               Объединение возможностей

# Комбинируя пользовательские классы исключений с пользовательскими моделями реагирования на ошибки, вы можете точно
# контролировать содержимое ответов об ошибках для различных типов исключений. Такой подход гарантирует, что сообщения
# об ошибках будут точными и непротиворечивыми.

#                                   Интернационализация (i18n) для сообщений об ошибках

# В FastAPI можно добавить интернационализацию (i18n), позволяющую доставлять сообщения об ошибках на нескольких
# языках в зависимости от языкового стандарта пользователя, что является хорошей практикой во взаимодействии с
# пользователями.
#
# Прочитайте, к примеру, про библиотеку fastapi_localization.

#                                      Коды ответов на запросы и ошибки, метаданные

# Пользовательские ответы об ошибках должны включать соответствующие коды состояния HTTP, указывающие на характер
# ошибки. Кроме того, вы можете включать метаданные в ответы об ошибках, такие как например временные метки, чтобы
# помочь в устранении неполадок и анализе ошибок.
#
# Кратко о значениях кодов:
#
# 1XX – статус-коды информационного типа. Они редко используются разработчиками напрямую. Ответы с этими кодами не
# могут иметь тела.
# 2XX – статус-коды, сообщающие об успешной обработке запроса. Они используются чаще всего.
# 3XX – статус-коды, сообщающие о перенаправлениях. Ответы с этими кодами статуса могут иметь или не иметь тело, за
# исключением ответов со статусом 304, "Not Modified", у которых не должно быть тела.
# 4XX – статус-коды, сообщающие о клиентской ошибке. Это ещё одна наиболее часто используемая категория.
# 5XX – статус-коды, сообщающие о серверной ошибке. Они почти никогда не используются разработчиками напрямую. Когда
# что-то идет не так в какой-то части кода вашего приложения или на сервере, он автоматически вернёт один из 5XX кодов.
# Продвинутый пример. Представьте, что вы хотите вернуть стандартный HTTP статус код "OK" 200.
#
# Но если данных ранее не существовало, то вернуть HTTP статус код "CREATED" 201.
#
# При этом вам все ещё необходимо иметь возможность фильтровать и конвертировать данные, которые вы возвращаете при
# помощи response_model.
#
# Для этого вы можете использовать Response параметр:
#
# from fastapi import FastAPI, Response, status
# app = FastAPI()
#
# tasks = {"foo": "Listen to the Bar Fighters"}
#
#
# @app.put("/get-or-create-task/{task_id}", status_code=200)
# def get_or_create_task(task_id: str, response: Response):
#     if task_id not in tasks:
#         tasks[task_id] = "This didn't exist before"
#         response.status_code = status.HTTP_201_CREATED
#     return tasks[task_id]
# И потом вы можете вернуть любой объект, который вам нужно (словарь, database model, и тд.). При этом ваша
# response_model будет иметь возможность фильтровать и конвертировать данные как обычно.

#                          Добавление кастомных заголовков при расширении информации об ошибках

# Вы можете добавить кастомные (пользовательские) заголовки в вашем FastAPI приложении. Это может потребоваться,
# например, для некоторых типов обеспечения безопасности.
#
# Этого можно добиться, например, так:
#
# from fastapi import FastAPI, HTTPException
#
# app = FastAPI()
#
# items = {"foo": "The Foo Wrestlers"}
#
#
# @app.get("/items-header/{item_id}")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
#         )
#     return {"item": items[item_id]}
# В данном примере мы расширили класс HTTPException, добавив заголовок "X-Error".

#                               Переопределение исключений проверки (валидации) запроса

# Когда запрос содержит недопустимые данные, Fast API автоматически выдает ошибку проверки запроса.
#
# И он также включает в себя обработчик исключений по умолчанию для него.
#
# Чтобы переопределить его, импортируйте RequestValidationError и используйте с помощью
# @app.exception_handler(RequestValidationError) для оформления обработчика исключений.
#
# Обработчик исключений получит Request и само исключение. Таким образом можно переопределить (расширить) не только
# класс HTTPException.
#
# from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException
#
# app = FastAPI()
#
#
# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}

#                                 Повторно используйте обработчики исключений FastAPI

# Если вы хотите использовать исключение вместе с теми же обработчиками исключений по умолчанию из Fast API, вы
# можете импортировать и повторно использовать обработчики исключений по умолчанию из fastapi.exception_handlers:
#
# from fastapi import FastAPI, HTTPException
# from fastapi.exception_handlers import (
#     http_exception_handler,
#     request_validation_exception_handler,
# )
# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException as StarletteHTTPException
#
# app = FastAPI()
#
#
# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)
#
#
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}

#                                               Задача на программирование

# Для этой задачи программирования вам необходимо реализовать пользовательские ответы на ошибки в приложении FastAPI,
# чтобы обеспечить более удобную и информативную обратную связь для пользователей.
#
# Требования:
#
# 1. Создайте приложение FastAPI по крайней мере с двумя конечными точками, которые выполняют разные задачи (например,
# одна конечная точка обрабатывает регистрацию пользователя, а другая конечная точка извлекает пользовательские данные).
#
# 2. Определите пользовательские модели реагирования на ошибки с помощью Pydantic для распространенных типов ошибок,
# которые могут возникать в приложении (например, `ErrorResponseModel` с полями для `status_code`, `message` и
# `error_code`).
#
# 3. Реализуйте пользовательские классы исключений для конкретных сценариев (например, `UserNotFoundException`,
# `InvalidUserDataException`), которые вызывают соответствующие HTTPExceptions с кодами состояния и пользовательскими
# сообщениями об ошибках.
#
# 4. Добавьте пользовательский заголовок "X-ErrorHandleTime", который указывает время, ушедшее на обработку ошибки,
# интернационализацию ответов на ошибки (второе по желанию).
#
# 5. Создайте пользовательские обработчики исключений, используя декоратор `@app.exception_handler`, чтобы
# перехватывать и обрабатывать пользовательские исключения. Обработчики должны генерировать пользовательские ответы
# на ошибки, используя определенные модели ответов.
#
# 6. Протестируйте пользовательские ответы на ошибки, отправив запросы к конечным точкам с неверными данными или
# несуществующими ресурсами. Убедитесь, что ответы об ошибках содержат ожидаемые коды состояния, сообщения об ошибках
# и коды кодов ошибок.
#
# Резюме:
#
# После выполнения задачи у вас должно быть приложение FastAPI, которое предоставляет пользовательские ответы на
# ошибки для различных типов исключений. Когда пользователи сталкиваются с ошибками, они должны получать информативные
# сообщения об ошибках, расширяющие их понимание проблем и улучшающие общий пользовательский опыт.

#                                               Вариант 1

# Модели:
#
# class User(BaseModel):
#     username: str
#     email: EmailStr
#     password: constr(min_length=4, max_length=8)
#
# class ErrorResponseModel(BaseModel):
#     detail: str
#     error_code: str
#     status_code: int
#
# Конечные точки:
#
# class UserNotFoundException(HTTPException):
#     def __init__(self, detail: str, error_code: str, status_code: int = 404):
#         self.error_code = error_code
#         super().__init__(detail=detail, status_code=status_code)
#
#
# class InvalidUserDataException(HTTPException):
#     def __init__(self, detail: str, error_code: str, status_code: int = 400):
#         self.error_code = error_code
#         super().__init__(detail=detail, status_code=status_code)
#
#
# field_error_messages = {
#     "username": "Должна быть строка",
#     "email": "Неверный формат email",
#     "password": "Пароль должен быть min 4 символа max 8"
# }
#
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     errors = []
#     for error in exc.errors():
#         field_name = error["loc"]
#         field_type = error["type"]
#         error_msg = field_error_messages.get(field_name, {key: value for key, value in field_error_messages.items() if key in field_name})
#         errors.append({"message": error_msg, "error_code": field_type})
#
#     return JSONResponse(status_code=400, content={"errors": errors})
#
#
# @app.exception_handler(UserNotFoundException)
# async def not_found_exception_handler(request: Request, exc: ErrorResponseModel):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail, "type_error": exc.error_code}
#     )
#
# @app.exception_handler(InvalidUserDataException)
# async def invalid_user_exception_handler(request: Request, exc: ErrorResponseModel):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail, "type_error": exc.error_code}
#     )
#
# users_db = {}
#
# @app.post("/register")
# async def create_user(user: User):
#     if user.username in users_db:
#         raise InvalidUserDataException(
#             detail="Имя пользователя уже занято",
#             error_code="Имя занято",
#             status_code=400
#         )
#     users_db[user.username] = user
#     return {"message": "User registered successfully"}
#
#
# @app.get("/users")
# async def get_user(username: str):
#     if username not in users_db:
#         raise UserNotFoundException(
#             detail="Пользователя с таким именем не существует",
#             error_code="Пользователь не существует",
#             status_code=404
#         )
#     return {"user": users_db[username]}
#
#
# @app.middleware("http")
# async def add_custom_headers(request, call_next):
#     start_time = datetime.utcnow()
#     response = await call_next(request)
#     end_time = datetime.utcnow()
#     process_time = (end_time - start_time).microseconds
#     response.headers["X-ErrorHandleTime"] = str(process_time)
#     return response

#                                                Вариант 2

# import uvicorn
#
# from fastapi import FastAPI, HTTPException, Request, status
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, EmailStr
# import time
#
# app = FastAPI()
#
#
# class User(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
#
#
# class UserModel(BaseModel):
#     id: int
#     name: str
#     email: EmailStr
#     password: str
#
#
# class UserResponse(BaseModel):
#     id: int
#     name: str
#     email: EmailStr
#
#
# users_db: dict[int, UserModel] = {}
#
#
# def id_generator() -> int:
#     counter = max(users_db.keys()) if users_db else 0
#     while True:
#         counter += 1
#         yield counter
#
#
# id_gen = id_generator()
#
#
# class ErrorResponseModel(BaseModel):
#     status_code: int
#     detail: str
#     errors: list[str]
#
#
# class UserNotFoundException(HTTPException):
#     def __init__(self, errors: list[str]):
#         super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#         self.errors = errors
#
#
# class InvalidUserDataException(HTTPException):
#     def __init__(self, errors: list[str]):
#         super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid user data")
#         self.errors = errors
#
#
# @app.exception_handler(UserNotFoundException)
# async def user_not_found_exception_handler(request: Request, exc: ErrorResponseModel):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.detail, "errors": exc.errors}
#     )
#
#
# @app.exception_handler(InvalidUserDataException)
# async def invalid_user_data_exception_handler(request: Request, exc: ErrorResponseModel):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.detail, "errors": exc.errors}
#     )
#
#
# @app.middleware("http")
# async def additional_processing(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     if response.status_code // 100 == 4:
#         response.headers["X-ErrorHandleTime"] = str(process_time)
#     return response
#
#
# def _check_user(user: User) -> None:
#     errors: list[str] = []
#     for db_user in users_db.values():
#         if user.name == db_user.name:
#             errors.append("Not unique name")
#         if user.email == db_user.email:
#             errors.append("Not unique email")
#     if len(errors) > 0:
#         raise InvalidUserDataException(errors)
#
#
# def _get_user_by_id(user_id: int) -> UserModel:
#     if user_id not in users_db:
#         errors = [f"User with id={user_id} not found"]
#         raise UserNotFoundException(errors)
#     return users_db[user_id]
#
#
# def _get_user_by_email(email: str) -> UserModel:
#     for db_user in users_db.values():
#         if email == db_user.email:
#             return db_user
#     errors = [f"User with email={email} not found"]
#     raise UserNotFoundException(errors)
#
#
# def _user_response(db_user: UserModel) -> UserResponse:
#     user_dict = db_user.model_dump()
#     del user_dict["password"]
#     return UserResponse(**user_dict)
#
#
# @app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# async def create_user(user: User):
#     _check_user(user)
#     db_user = UserModel(id=next(id_gen), name=user.name, email=user.email, password=user.password)
#     users_db[db_user.id] = db_user
#     return _user_response(db_user)
#
#
# @app.get("/users/{user_id}", response_model=UserResponse)
# async def read_user_by_id(user_id: int):
#     db_user = _get_user_by_id(user_id)
#     return _user_response(db_user)
#
#
# @app.get("/users/by_email/{email}", response_model=UserResponse)
# async def read_user_by_email(email: str):
#     db_user = _get_user_by_email(email)
#     return _user_response(db_user)
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)

