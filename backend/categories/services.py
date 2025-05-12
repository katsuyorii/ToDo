from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import CategoryModel
from .schemas import CategoryCreateSchema
from .utils import get_category_by_id
from .exceptions import CATEGORY_NOT_FOUND


async def read_categories(db: AsyncSession) -> list[CategoryModel]:
    result = await db.execute(select(CategoryModel))
    return result.scalars().all()

async def read_category(category_id: int, db: AsyncSession) -> CategoryModel | None:
    category = await get_category_by_id(category_id, db)

    if category is None:
        raise CATEGORY_NOT_FOUND

    return category
    
async def add_category(category_data: CategoryCreateSchema, db: AsyncSession) -> CategoryModel:
    new_category = CategoryModel(**category_data.model_dump())

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    return new_category

async def remove_category(category_id: int, db: AsyncSession) -> None:
    category = await get_category_by_id(category_id, db)

    if category is None:
        raise CATEGORY_NOT_FOUND
    
    await db.delete(category)
    await db.commit()