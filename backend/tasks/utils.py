from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from .models import TaskModel


async def get_task_by_id(task_id: int, db: AsyncSession) -> TaskModel | None:
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id).options(selectinload(TaskModel.category)))
    
    return result.scalar_one_or_none()