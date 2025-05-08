from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import TaskModel
from .schemas import TaskCreateSchema, TaskUpdateSchema
from .utils import get_task_by_id
from .exceptions import TASK_NOT_FOUND


async def read_tasks(db: AsyncSession) -> list[TaskModel]:
    result = await db.execute(select(TaskModel))
    return result.scalars().all()

async def read_task(task_id: int, db: AsyncSession) -> TaskModel | None:
    task = await get_task_by_id(task_id, db)

    if task is None:
        raise TASK_NOT_FOUND
    
    return task

async def add_task(task_data: TaskCreateSchema, db: AsyncSession) -> TaskModel:
    new_task = TaskModel(**task_data.model_dump(exclude_unset=True))

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task

async def remove_task(task_id: int, db: AsyncSession) -> None:
    task = await get_task_by_id(task_id, db)

    if task is None:
        raise TASK_NOT_FOUND
    
    await db.delete(task)
    await db.commit()

async def edit_task(task_id: int, updated_task_data: TaskUpdateSchema, db: AsyncSession) -> TaskModel | None:
    task = await get_task_by_id(task_id, db)

    if task is None:
        raise TASK_NOT_FOUND
    
    for key, value in updated_task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)

    return task