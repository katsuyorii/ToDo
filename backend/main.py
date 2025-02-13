import uvicorn
from fastapi import FastAPI
from routers.task import task_router


app = FastAPI()
app.include_router(task_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)