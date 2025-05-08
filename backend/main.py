from fastapi import FastAPI

from tasks.routers import tasks_router


app = FastAPI()

app.include_router(tasks_router)