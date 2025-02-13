from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from typing import List
from schemas.task import TaskResponseSchema, TaskCreateSchema
from database.database import get_session
from services.task import TaskService


task_router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)

@task_router.get('/', response_model=List[TaskResponseSchema])
async def get_tasks(db_session: AsyncSession = Depends(get_session)):
    task_service = TaskService(db_session)
    tasks = await task_service.get_all_tasks()

    return tasks

@task_router.post('/', status_code=201, response_model=TaskResponseSchema)
async def create_task(task: TaskCreateSchema, db_session: AsyncSession = Depends(get_session)):
    task_service = TaskService(db_session)
    new_task = await task_service.create_task(task)

    return new_task