from fastapi import FastAPI

from app.chapter_3.router import router as router_3
from app.chapter_4.router import router as router_4
from app.chapter_5.router import router as router_5
from app.chapter_6.router import router as router_6
from app.chapter_7.router import router as router_7

app = FastAPI(
    title="FastAPI на Stepik"
)

app.include_router(router_3)
app.include_router(router_4)
app.include_router(router_5)
app.include_router(router_6)
app.include_router(router_7)

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/sum/")
# def calculate_sum(a: int, b: int):
#     return {"result": a + b}
