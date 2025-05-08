from fastapi import APIRouter, Depends

from src.dependency import get_db

from .schemas import TaskCreate, TaskResponse
from .services import read_tasks, add_task

from sqlalchemy.ext.asyncio import AsyncSession


tasks_router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)

@tasks_router.get('/', response_model=list[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await read_tasks(db)

@tasks_router.post('/', response_model=TaskResponse)
async def create_task(task_data: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await add_task(task_data, db)
