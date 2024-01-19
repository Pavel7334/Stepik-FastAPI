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

#                                           Соображения безопасности

# """Хотя базовая аутентификация проста в реализации, она имеет некоторые ограничения безопасности, такие как передача
#
# учетных данных в виде обычного текста. Для более безопасных механизмов аутентификации вы можете изучить аутентификацию
#
# на основе JWT или интегрировать сторонние поставщики аутентификации, такие как OAuth.
#
# В этом уроке мы рассмотрели основы реализации базовой аутентификации в FastAPI. Мы узнали, как работает базовая
#
# аутентификация, и шаг за шагом интегрировали ее в наше приложение FastAPI для защиты конкретной конечной точки. Не
#
# забывайте внимательно относиться к аутентификации и рассмотрите более продвинутые методы для готовых к работе
#
# приложений. В следующем уроке мы рассмотрим аутентификацию на основе JWT, популярную и более безопасную альтернативу
#
# базовой аутентификации."""

#                                                   4.2

#                                   Что такое аутентификация на основе JWT?

# """JWT расшифровывается как веб-токен JSON, и это популярный метод реализации аутентификации в веб-приложениях. В
#
# отличие от базовой аутентификации, где серверу необходимо поддерживать состояние (обычно с помощью сессионных файлов
#
# cookie или токенов), JWT допускает аутентификацию без сохранения состояния. При настройке без сохранения состояния
#
# серверу не нужно хранить пользовательскую информацию, что делает его масштабируемым и подходящим для распределенных
#
# систем."""

#                                           Как работает JWT?

# import jwt  # тут используем библиотеку PyJWT
#
# # Секретный ключ для подписи и верификации токенов JWT
# SECRET_KEY = "mysecretkey"  # тут мы в реальной практике используем что-нибудь вроде команды Bash (Linux)
# # 'openssl rand -hex 32', и храним очень защищенно
# ALGORITHM = "HS256"  # плюс в реальной жизни мы устанавливаем "время жизни" токена
#
# # Пример информации из БД
# USERS_DATA = [
#     {"username": "admin", "password": "adminpass"}
# ]  # в реальной БД мы храним только ХЭШИ паролей (можете прочитать про библиотеку, к примеру, 'passlib') + соль
#
#
# # (известная только нам добавка к паролю)
#
#
# # Функция для создания JWT токена
# def create_jwt_token(data: dict):
#     return jwt.encode(data, SECRET_KEY,
#                       algorithm=ALGORITHM)  # кодируем токен, передавая в него наш словарь с тем, что мы
#     # хотим там разместить
#
#
# # Функция получения User'а по токену
# def get_user_from_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # декодируем токен
#         return payload.get(
#             "sub")  # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно
#         # там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое, что мы
#         # сами туда кладем
#     except jwt.ExpiredSignatureError:
#         pass  # тут какая-то логика ошибки истечения срока действия токена
#     except jwt.InvalidTokenError:
#         pass  # тут какая-то логика обработки ошибки декодирования токена
#
#
# # Функция для получения пользовательских данных на основе имени пользователя
# def get_user(username: str):
#     for user in USERS_DATA:
#         if user.get("username") == username:
#             return user
#     return None
#
#
# # закодируем токен, внеся в него словарь с утверждением о пользователе
# token = create_jwt_token({"sub": "admin"})
#
# print(token)  # можете посмотреть как выглядит токен jwt
#
# # декодируем токен и излечем из него информацию о юзере, которую мы туда зашили
# username = get_user_from_token(token)
#
# print(username)  # посмотрим, что возвращается то, что ожидаем
#
# # и теперь пойдем в нашу базу данных искать такого юзера по юзернейму
# current_user = get_user(username)
#
# print(current_user)  # удостоверимся, что нашелся тот, кто нужен

#                                           Рабочий процесс JWT

"""Рабочий процесс аутентификации на основе JWT выглядит следующим образом:

Шаг 1: Аутентификация пользователя. Когда пользователь предоставляет действительные учетные данные (например, имя 

пользователя и пароль) для входа в систему, сервер проверяет их и генерирует JWT.
Шаг 2: Отправка JWT клиенту. Сервер отправляет JWT обратно клиенту (обычно в заголовке `Authorization` ответа) в 

качестве токена.
Шаг 3: Последующие запросы. Для всех последующих запросов, требующих аутентификации, клиент отправляет JWT в 

заголовке `Authorization`. Затем сервер проверяет подпись JWT с помощью секретного ключа. Если подпись действительна, 

сервер извлекает информацию о пользователе из утверждений и разрешает доступ к запрошенным ресурсам."""

#                                    Преимущества аутентификации на основе JWT

"""- Без сохранения состояния: серверу не нужно хранить информацию о сеансе, что делает его более масштабируемым для 

распределенных систем.

- Междоменность (кросс-доменность): Поскольку JWT обычно отправляются в заголовке "Авторизация" (Authorization), 

они хорошо работают с CORS (совместное использование ресурсов разных источников - Cross-Origin Resource Sharing) и 

могут использоваться в разных доменах.

- Пользовательские утверждения: Вы можете добавлять пользовательские утверждения в полезную нагрузку, обеспечивая 

гибкое хранение пользовательской информации."""

#                                           Соображения безопасности

# Хотя аутентификация на основе JWT дает множество преимуществ, она также сопряжена с соображениями безопасности:
# - Срок действия токена: установите подходящее время истечения срока действия токена, чтобы ограничить его срок
# действия.
# - Используйте HTTPS: Всегда используйте HTTPS для шифрования связи между клиентом и сервером.
# - Защита секретного ключа: Сохраняйте секретный ключ, используемый для подписи JWT, в безопасности. Компрометация
# ключа может привести к нарушениям безопасности.
# - Размер токена: Помните о размере токена, поскольку он отправляется с каждым запросом. Избегайте включения
# конфиденциальных или ненужных данных в полезную нагрузку.
#
# На следующем уроке мы рассмотрим управление доступом на основе ролей, которое позволяет детально управлять
# разрешениями в вашем приложении FastAPI.
#
# Примечание: Помните, что реализация аутентификации на основе JWT в производственной среде может потребовать
# дополнительных соображений, таких как механизмы отзыва токенов и обновления.

#                                           Пример более продвинутой защиты

"""Иногда нужно быстро сделать аутентификацию, используя имя пользователя и пароль (например, при разработке внутри 
компании). Для этого можно использовать возможности FastAPI по работе с OAuth2: """

# from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel
# import jwt
#
# app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#
# # Секретный ключ для подписи и верификации токенов JWT
# SECRET_KEY = "mysecretkey"  # тут мы в реальной практике используем что-нибудь вроде команды Bash (Linux)
# # 'openssl rand -hex 32', и храним очень защищенно
# ALGORITHM = "HS256"  # плюс в реальной жизни мы устанавливаем "время жизни" токена
#
# # Пример информации из БД
# USERS_DATA = [
#     {"username": "admin", "password": "adminpass"}
# ]  # в реальной БД мы храним только ХЭШИ паролей (можете прочитать про библиотеку, к примеру, 'passlib') + соль
# # (известная только нам добавка к паролю)
#
#
# class User(BaseModel):
#     username: str
#     password: str
#
#
# # Функция для создания JWT токена
# def create_jwt_token(data: dict):
#     return jwt.encode(data, SECRET_KEY,
#                       algorithm=ALGORITHM)  # кодируем токен, передавая в него наш словарь с тем, что мы хотим там
#                                             # разместить
#
#
# # Функция получения User'а по токену
# def get_user_from_token(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # декодируем токен
#         return payload.get(
#             "sub")  # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно
#         # там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое,
#         # что мы сами туда кладем
#     except jwt.ExpiredSignatureError:
#         pass  # тут какая-то логика ошибки истечения срока действия токена
#     except jwt.InvalidTokenError:
#         pass  # тут какая-то логика обработки ошибки декодирования токена
#
#
# # Функция для получения пользовательских данных на основе имени пользователя
# def get_user(username: str):
#     for user in USERS_DATA:
#         if user.get("username") == username:
#             return user
#     return None
#
#
# # роут для аутентификации; так делать не нужно, это для примера - более корректный пример в следующем уроке
# @app.post("/login")
# async def login(user_in: User):
#     for user in USERS_DATA:
#         if user.get("username") == user_in.username and user.get("password") == user_in.password:
#             return {"access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer"}
#     return {"error": "Invalid credentials"}
#
#
# # защищенный роут для получения информации о пользователе
# @app.get("/about_me")
# async def about_me(current_user: str = Depends(get_user_from_token)):
#     user = get_user(current_user)
#     if user:
#         return user
#     return {"error": "User not found"}

# В этом примере мы создали два маршрута (login для получения JWT токена при предоставлении валидным данных, и
# защищенный about_me, который через зависимость проверяет существование юзера по токену).
#
# OAuth2PasswordBearer проверяет схему направления токена (Authorization: Bearer) и возвращает токен. В нем мы
# передаем параметр tokenUrl, который указывает наш маршрут для создания токена (если не рассматривать наш тестовый
# пример, то обычно по такому маршруту зависимость с формой авторизации, то есть сразу оно перенаправит сразу на ввод
# пользовательских данных - либо вернёт токен, если его прислали, либо попросит ввести логин/пароль). Пример с
# формой - в следующем уроке. Сейчас наша задача пока понять логику работы.
#
# Такой пример улучшит защиту вашего приложения (по сравнению с базовой аутентификацией), хотя настоятельно
# рекомендуем вам не ограничиваться полученной в данном курсе информацией, а детально изучить технологии OAuth2 и
# JWT и прочее в разделах "Безопасность" обычного и продвинутого руководства пользователя FastAPI по
# адресам: https://fastapi.tiangolo.com/tutorial/security/  и https://fastapi.tiangolo.com/advanced/security/


#                                    Задача на программирование повышенной сложности
#                                                 ПЕРВОЕ РЕШЕНИЕ
# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# import jwt
# from datetime import datetime, timedelta
# from passlib.context import CryptContext
# import secrets
#
# from sqlalchemy.orm import Session
#
# from app.dataclasses import models
# from app.db.session_local import session_local
#
# app = FastAPI()
#
#
# def get_db():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# SECRET_KEY = "dba749b064fa8502475b7bd8b31b81d2cb20a34fbfee762ba4ba9c09093c799a"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 1
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
#
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)
#
#
# def get_password_hash(password):
#     return pwd_context.hash(password)
#
#
# def get_user(username: str, db: Session = Depends(get_db)):
#     return (db.query(models.User)
#             .filter(models.User.username == username).first())
#
#
# def authenticate_user(db, username: str, password: str):
#     user = get_user(username, db)
#     if not user or not verify_password(password, user.password):
#         return False
#     return True
#
#
# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
#
#
# @app.post("/login")
# async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     username = form_data.username
#     password = form_data.password
#
#     if not authenticate_user(db, username, password):
#         raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
#
#     access_token = create_access_token(data={"sub": username})
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# @app.get("/protected_resource")
# async def protected_resource(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
#     except jwt.DecodeError:
#         raise HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})
#
#     return {"message": "Access granted to protected resource"}

#                                           ВТОРОЕ РЕШЕНИЕ

# from fastapi import FastAPI, Depends
# from models import *
# from fastapi.security import  OAuth2PasswordBearer
# import jwt
#
# app = FastAPI()
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# SECRET_KEY = "sectret"
# ALGORITHM = "HS256"
# users_bd = [User(login="vasya", password="31maet"), User(login="masha", password="qwerty")]
#
# @app.post("/login")
# def user_login(user_in: User):
#     for user in users_bd:
#         if user.login == user_in.login and user.password == user_in.password:
#             return {"access_token": create_jwt_token({"sub": user_in.login}), "token_type": "bearer"}
#     return {"error": "Invalid credentials"}
#
# @app.get("/user", response_model=Dict[str, str] | User_Out)
# def read_users(current_user: str = Depends(oauth2_scheme)):
#     user = get_user(get_user_from_token(current_user))
#     if user:
#         return user
#     return {"error": "User not found"}

#                                               ТРЕТЬЕ РЕШЕНИЕ

# import sys
# from typing import Annotated
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# import jwt
# import pydantic
# import logging
#
#
# # Секретный ключ для подписи и верификации токенов JWT
# SECRET_KEY = "mysecretkey"
# ALGORITHM = "HS256"
#
# class User(pydantic.BaseModel):
#     username: str
#     password: str
#
# user_db = [User(username='user1', password='123'), User(username='user2', password='456')]
#
# app = FastAPI()
# oauth2_security = OAuth2PasswordBearer(tokenUrl='login')
# logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s', level=logging.DEBUG)
# # logging.debug(f"{user_db=}")
#
#
# def check_user(username: str, password: str) -> User | None:
#     """Возвращает User, если есть с таким логином и паролем, либо None"""
#     user = None
#     for item in user_db:
#         # print(f"check_user: {item.username=}, {username=}")
#         if item.username == username:
#             if item.password == password:
#                 user = item
#                 logging.debug(f"check_user: {username!r} is verified")
#                 return user
#             logging.debug(f"check_user: invalid password for {username!r}")
#             return None
#     return None
#
#
# def get_user(username: str) -> User | None:
#     for user in user_db:
#         if user.username == username:
#             return user
#     return None
#
#
# def create_jwt_token(data: dict):
#     return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
#
#
# @app.post('/login')
# def post_login(credentials: User):
#     user = check_user(credentials.username, credentials.password)
#     if user is None:
#         raise HTTPException(
#             status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect user or password",
#             )
#     data = {'username': user.username}
#     token = create_jwt_token(data)
#     logging.info(f"post_login: access granted for {user.username}, {token=}")
#     return {"access_token": token, "token_type": "bearer"}
#
#
# def get_user_from_token(token: Annotated[str, Depends(oauth2_security)]) -> User:
#     try:
#         logging.debug(f"get_user_from_token: {token=}")
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         # print(f"get_user_from_token: {payload=}")
#         username = payload.get('username')
#         logging.debug(f"get_user_from_token: {username=}")
#         return get_user(username)
#     except jwt.ExpiredSignatureError as e:
#         logging.debug(f"get_user_from_token: access denied", exc_info=e)
#         raise HTTPException(
#             status.HTTP_401_UNAUTHORIZED,
#             detail="Token expired",
#             )
#     except jwt.InvalidTokenError as e:
#         logging.debug(f"get_user_from_token: access denied", exc_info=e)
#         raise HTTPException(
#             status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             )
#
#
# @app.get('/protected_resource')
# def get_protected_resource(current_user: Annotated[User, Depends(get_user_from_token)]):
#     logging.info(f"Access granted for {current_user.username!r}")
#     return {"Message": f"Access granted for {current_user.username!r}"}

#                                                   4.3

#                                   Понимание управления доступом на основе ролей (RBAC)

"""Понимание управления доступом на основе ролей (RBAC)
Управление доступом на основе ролей (RBAC - Role Based Access Control) - это мощный подход к управлению разрешениями 
в веб-приложениях. Он обеспечивает гибкий и масштабируемый способ назначения определенных ролей пользователям, 
предоставляя им доступ только к тем ресурсам и действиям, которые соответствуют их роли или уровню авторизации. RBAC 
упрощает процесс предоставления и отзыва прав доступа на основе предопределенных ролей, снижая риск 
несанкционированного доступа."""

#                                               Компоненты RBAC

"""RBAC обычно состоит из следующих компонентов:

Роли: Роли определяются на основе обязанностей пользователя или должностных функций. С каждой ролью связаны 
определенные разрешения, которые определяют, какие действия может выполнять пользователь.

Разрешения: Разрешения представляют собой отдельные действия или операции, которые пользователь может выполнять в 
приложении. Например, разрешение "чтение" позволяет пользователю просматривать данные, в то время как разрешение 
"запись" предоставляет возможность изменять данные.

Пользователи: Пользователям назначается одна или несколько ролей, в зависимости от их обязанностей и требований к 
доступу"""

#                                           Внедрение RBAC в FastAPI

"""Чтобы реализовать RBAC в приложении FastAPI, мы можем использовать комбинацию механизмов аутентификации (например, 
аутентификацию на основе JWT) и пользовательскую логику авторизации. Вот высокоуровневый обзор того, как может быть 
реализован RBAC:

Шаг 1: Определите роли и разрешения. Определите роли и соответствующие им разрешения, которые соответствуют 
требованиям приложения. Например, у вас могут быть такие роли, как "администратор", "пользователь" и "гость", каждая 
из которых имеет определенные разрешения.

Шаг 2: Свяжите роли с пользователями. Назначайте роли пользователям в процессе регистрации пользователя или на основе 
их атрибутов. Например, пользователь с правами администратора может иметь роль "администратор", в то время как обычный 
пользователь имеет роль "пользователь".

Шаг 3: Авторизация на основе ролей. Создайте логику авторизации, которая проверяет роль пользователя и необходимые 
разрешения, прежде чем разрешить доступ к определенным ресурсам или конечным точкам. Например, пользователь с правами 
администратора может иметь доступ к созданию и удалению ресурсов, в то время как обычный пользователь может только 
читать и обновлять их."""

#                                       Обработка доступа на основе ролей

"""FastAPI предоставляет различные механизмы для управления доступом на основе ролей, такие как:
Внедрение зависимостей: Система внедрения зависимостей FastAPI позволяет создавать пользовательские зависимости, 
которые проверяют роль пользователя перед предоставлением доступа к определенным конечным точкам.
Авторизация на основе декоратора: Вы можете использовать декораторы Python для определения авторизации на основе 
ролей для определенных конечных точек, что упрощает управление доступом на уровне конечной точки.
Интеграция с базой данных: Объедините RBAC с базой данных вашего приложения для хранения ролей пользователей и 
связанных с ними разрешений."""

#                              Более глубокое понимание управления доступом на основе ролей (RBAC)

"""Как вы могли понять, управление доступом на основе ролей (RBAC - Role Based Access Control) - это мощный подход к 
управлению разрешениями в веб-приложениях. Он обеспечивает гибкий и масштабируемый способ назначения определенных 
ролей пользователям, предоставляя им доступ только к тем ресурсам и действиям, которые соответствуют их роли или 
уровню авторизации. RBAC упрощает процесс предоставления и отзыва прав доступа на основе предопределенных ролей, 
снижая риск несанкционированного доступа."""

"""Давайте рассмотрим довольно объёмный пример кода реализации (хотя если вы выполняли предыдущее задание, то 
перекопали намного больше информации по JWT и теперь можете сделать реальную защиту для FastAPI приложения):"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # для реквест-формы нам нужно установить
# доп. библиотеку командой pip install python-multipart
from pydantic import BaseModel
import jwt
from typing import Optional, Annotated
'''тут работаем с библиотекой PyJWT, 
но в реальной жизни вы скорее всего предпочтете 'python-jose', которая чуть шире PyJWT и рекомендуется самими FastAPI
'''

app = FastAPI()

# Секретный ключ для подписи и верификации токенов JWT
SECRET_KEY = "mysecretkey" # тут мы в реальной практике используем что-нибудь вроде команды Bash (Linux) 'openssl
# rand -hex 32', и храним очень защищенно
ALGORITHM = "HS256" # плюс в реальной жизни мы устанавливаем "время жизни" токена

# Пример информации из БД
USERS_DATA = {
    "admin": {"username": "admin", "password": "adminpass", "role": "admin"},
    "user": {"username": "user", "password": "userpass", "role": "user"},
} # в реальной БД мы храним только ХЭШИ паролей (можете прочитать про библиотеку, к примеру, 'passlib') + соль
# (известная только нам добавка к паролю)

# OAuth2PasswordBearer для авторизации по токену
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Модель User для аутентификации (если делали задание по JWT, то тут добавляем только роль)
class User(BaseModel):
    username: str
    password: str
    role: Optional[str] = None


# Функция для создания JWT токена
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


# Функция получения User'а по токену - это скорее всего была самая сложная часть в предыдущем задании
def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # декодируем токен
        return payload.get("sub") # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о
        # юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время
        # 'сгорания' и другое, что мы сами туда кладем
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# Функция для получения пользовательских данных на основе имени пользователя
def get_user(username: str):
    if username in USERS_DATA:
        user_data = USERS_DATA[username]
        return User(**user_data)
    return None


# Роут для получения JWT-токена (так работает логин)
@app.post("/token/")
def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]): # тут логинимся через форму
    user_data_from_db = get_user(user_data.username)
    if user_data_from_db is None or user_data.password != user_data_from_db.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": create_jwt_token({"sub": user_data.username})} # тут мы добавляем полезную нагрузку в
    # токен, и говорим, что "sub" содержит значение username


# Защищенный роут для админов, когда токен уже получен
@app.get("/admin/")
def get_admin_info(current_user: str = Depends(get_user_from_token)):
    user_data = get_user(current_user)
    if user_data.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": "Welcome Admin!"}


# Защищенный роут для обычных пользователей, когда токен уже получен
@app.get("/user/")
def get_user_info(current_user: str = Depends(get_user_from_token)):
    user_data = get_user(current_user)
    if user_data.role != "user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": "Hello User!"}

"""П.С. для удобства восприятия мы приводим код единым текстом, хотя тут, по сути, файлы: main.py, routes.py, 
models.py, config.py, security.py, возможно имитация db.py. 

В этом примере мы определяем модель `User` для представления пользовательских данных с ролями (администратор или 
пользователь). Мы используем словарь `USERS_DATA` для хранения образцов пользовательских данных. Для простоты в этом 
примере мы не используем какую-либо базу данных (они будут рассмотрены в следующем модуле).

Маршрут `/token/` позволяет пользователям войти в систему и получить токен JWT. Токен используется для последующих 
запросов в качестве средства аутентификации. Обратно нам вернется токен.

Мы определяем два защищенных маршрута: "/admin/" и "/user/", для доступа к которым требуется аутентифицированный 
пользователь с соответствующими ролями. Например, в  Postman'е, мы отправляем GET-запрос, на вкладке Authorization 
выбираем тип "Bearer Token" и копируем полученный токен (без кавычек). Доступ открыт, поздравляю! 

Далее под капотом при получении GET-запроса мы используем функцию `Depends(get_user_from_token)` для извлечения 
пользовательских данных из токена JWT и проверки их ролей, прежде чем разрешить доступ к защищенным маршрутам.

Примечание: В реальном приложении важно использовать надлежащие меры безопасности и базу данных для безопасного 
хранения пользовательских данных и управления ими. Этот пример предназначен только для демонстрационных целей и 
может не подходить для производственного использования, поскольку он хранит пользовательские данные в памяти.

Плюс не забудьте про минимальную длину пароля пользователей (желательно 16 символов, включающих буквы, цифры и 
символы), а также установить блокировку (защиту) от подбора паролей (Х попытки и блок на ХХ минут), в т.ч. можно 
выписывать баны (включать в список заблокированных адресов). Про соль к паролю и прочее можете почитать тут:

https://habr.com/ru/companies/acribia/articles/413157/"""

