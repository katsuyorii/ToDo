from fastapi import APIRouter, Depends, status

from src.dependencies import get_db

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CategoryResponseSchema, CategoryCreateSchema
from .services import add_category


categories_router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
)

@categories_router.post('/', response_model=CategoryResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_category(category_data: CategoryCreateSchema, db: AsyncSession = Depends(get_db)):
    return await add_category(category_data, db)