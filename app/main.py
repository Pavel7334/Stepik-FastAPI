from fastapi import FastAPI

from app.chapter_3.router import router as router_3_1

app = FastAPI(
    title="FastAPI на Stepik"
)

app.include_router(router_3_1)

