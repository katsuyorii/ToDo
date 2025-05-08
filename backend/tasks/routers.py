from fastapi import APIRouter, Depends, status

from src.dependencies import get_db

from .schemas import TaskCreateSchema, TaskResponseSchema, TaskUpdateSchema
from .services import read_tasks, add_task, remove_task, edit_task

from sqlalchemy.ext.asyncio import AsyncSession


tasks_router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)

@tasks_router.get('/', response_model=list[TaskResponseSchema])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await read_tasks(db)

@tasks_router.post('/', response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreateSchema, db: AsyncSession = Depends(get_db)):
    return await add_task(task_data, db)

@tasks_router.patch('/{task_id}', response_model=TaskResponseSchema)
async def update_task(task_id: int, updated_task_data: TaskUpdateSchema, db: AsyncSession = Depends(get_db)):
    return await edit_task(task_id, updated_task_data, db)

@tasks_router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await remove_task(task_id, db)