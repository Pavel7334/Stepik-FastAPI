from fastapi import FastAPI

from app.chapter_3.router import router as router_3
from app.chapter_4.router import router as router_4


app = FastAPI(
    title="FastAPI на Stepik"
)

app.include_router(router_3)
app.include_router(router_4)

