from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from models.task import TaskModel, CategoryModel, TagModel


class TaskRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
    
    async def get_all_tasks(self) -> List[TaskModel]:
        result = await self.db_session.execute(select(TaskModel).options(selectinload(TaskModel.category), selectinload(TaskModel.tags)).order_by(TaskModel.id))
        
        return result.scalars().all()

    async def create_task(self, task: TaskModel) -> TaskModel:
        self.db_session.add(task)
        await self.db_session.flush()
        await self.db_session.commit()
        await self.db_session.refresh(task, attribute_names=["category", "tags"])

        return task