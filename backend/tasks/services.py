from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import TaskModel
from .schemas import TaskCreate


async def read_tasks(db: AsyncSession) -> list[TaskModel]:
    result = await db.execute(select(TaskModel))
    return result.scalars().all()

async def add_task(task_data: TaskCreate, db: AsyncSession) -> TaskModel:
    new_task = TaskModel(**task_data.model_dump(exclude_unset=True))

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task