from fastapi import FastAPI

from tasks.routers import tasks_router
from categories.routers import categories_router
from auth.routers import auth_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(categories_router)