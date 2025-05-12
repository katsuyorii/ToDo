from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import CategoryModel


async def get_category_by_id(category_id: int, db: AsyncSession) -> CategoryModel | None:
    result = await db.execute(select(CategoryModel).where(CategoryModel.id == category_id))
    
    return result.scalar_one_or_none()