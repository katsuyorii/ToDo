from fastapi import FastAPI

from tasks.routers import tasks_router
from categories.routers import categories_router


app = FastAPI()

app.include_router(tasks_router)
app.include_router(categories_router)