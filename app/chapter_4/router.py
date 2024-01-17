from fastapi import APIRouter

from app.chapter_4.models import User

router = APIRouter(
    prefix="/tasks",
    tags=["Chapter_4:"]
)

#                                                   4.1

#                                   Что такое аутентификация?

"""Аутентификация - это процесс проверки личности пользователя или системы, пытающихся получить доступ к 

веб-приложению. Это гарантирует, что только авторизованные пользователи смогут получить доступ к защищенным ресурсам 

или выполнить определенные действия. FastAPI поддерживает различные методы аутентификации, и одним из самых простых 

подходов является использование базовой аутентификации."""

#                                   Как работает базовая аутентификация?

"""Базовая аутентификация - это простой метод, при котором клиент (обычно веб-браузер или клиент API) вводит имя 

пользователя и пароль в заголовок запроса `Authorization`. Затем сервер проверяет эти учетные данные в базе данных 

пользователя или у поставщика аутентификации. FastAPI обеспечивает встроенную поддержку базовой аутентификации, что 

упрощает ее реализацию."""

#                                   Реализация базовой аутентификации в FastAPI

# from fastapi import Depends, status, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
#
# security = HTTPBasic()
#
# USER_DATA = [User(**{"username": "user1", "password": "pass1"}), User(**{"username": "user2", "password": "pass2"})]
#
#
# # симуляционный пример
# def get_user_from_db(username: str):
#     for user in USER_DATA:
#         if user.username == username:
#             return user
#     return None
#
#
# def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
#     user = get_user_from_db(credentials.username)
#     if user is None or user.password != credentials.password:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#     return user
#
#
# @router.get("/protected_resource/")
# def get_protected_resource(user: User = Depends(authenticate_user)):
#     return {"message": "You have access to the protected resource!", "user_info": user}
#
#
# """`Depends(authenticate_user)` - это пример внедрения зависимости (dependency injection), которые мы будем разбирать
#
# позднее в этом курсе. Для любознательных - можете заглянуть в комментарии, перескочить в урок 8.1 (8.1.2-8.1.3), или
#
# можете "поверить на слово", потом все встанет на свои места :)
#
# В приведенном выше коде мы сначала импортируем необходимые зависимости, включая `FastAPI`, `HTTPBasic` и
#
# `HTTPBasicCredentials`. Затем мы создаем экземпляр `HTTPBasic` для использования для аутентификации. Мы определяем
#
# функцию `authenticate_user`, которая принимает `HTTPBasicCredentials` в качестве параметра, полученного из запроса.
#
# Эта функция проверяет учетные данные пользователя по базе данных и выдает ошибку HTTP 401 Unauthorized, если они
#
# недействительны.
# Наконец, мы защищаем нашу конечную точку, добавляя функцию `authenticate_user` в качестве зависимости. Когда клиент
#
# отправляет запрос к конечной точке `/protected_resource/`, FastAPI сначала запустит функцию `authenticate_user`
#
# для проверки учетных данных пользователя, прежде чем выполнять основную функцию конечной точки."""

