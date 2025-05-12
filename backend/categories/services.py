from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import CategoryModel
from .schemas import CategoryCreateSchema


async def add_category(category_data: CategoryCreateSchema, db: AsyncSession) -> CategoryModel:
    new_category = CategoryModel(**category_data.model_dump())

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    return new_category