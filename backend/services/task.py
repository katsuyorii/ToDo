from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from repositories.task import TaskRepository
from models.task import TaskModel, TagModel
from schemas.task import TaskCreateSchema


class TaskService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.task_repo = TaskRepository(db_session)
    
    async def get_all_tasks(self) -> List[TaskModel]:
        return await self.task_repo.get_all_tasks()
    
    async def create_task(self, task: TaskCreateSchema) -> TaskModel:
        result = await self.db_session.execute(select(TagModel).filter(TagModel.id.in_(task.tags)))
        tags = result.scalars().all()

        task_dict = task.model_dump(exclude_unset=True)
        task_dict['tags'] = tags

        new_task = TaskModel(**task_dict)

        return await self.task_repo.create_task(new_task)