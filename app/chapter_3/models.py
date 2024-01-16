from pydantic import BaseModel


# class User(BaseModel):
#     name: str
#     id: int
#
#
# class FeedBack(BaseModel):
#     name: str
#     message: str


class User(BaseModel):
    username: str
    password: str

