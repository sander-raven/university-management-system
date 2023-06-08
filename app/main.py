from fastapi import FastAPI

from fastapi_pagination import add_pagination

from router import router

app = FastAPI()
add_pagination(app)

app.include_router(router)
