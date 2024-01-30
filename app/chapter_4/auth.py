from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt

from dao import UserDAO

SECRET_KEY = "0c7b523c661e1343c886d7cee9a358b26bcc2519946ad69fe9ba0cc163777c7b"
ALROGITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, password_db: str):
    return password == password_db


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, ALROGITHM
    )
    return encoded_jwt


def authenticate_user(username: str, password: str):
    user = UserDAO.get_user(username)
    if user and verify_password(password, user.password):
        return user
    return None