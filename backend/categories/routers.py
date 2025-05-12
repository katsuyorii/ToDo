from fastapi import APIRouter, Depends, status

from src.dependencies import get_db

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CategoryResponseSchema, CategoryCreateSchema, CategoryUpdateSchema
from .services import read_categories, read_category, add_category, remove_category, edit_category


categories_router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
)

@categories_router.get('/', response_model=list[CategoryResponseSchema])
async def get_categories(db: AsyncSession = Depends(get_db)):
    return await read_categories(db)

@categories_router.get('/{category_id}', response_model=CategoryResponseSchema)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    return await read_category(category_id, db)

@categories_router.post('/', response_model=CategoryResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_category(category_data: CategoryCreateSchema, db: AsyncSession = Depends(get_db)):
    return await add_category(category_data, db)

@categories_router.patch('/{category_id}', response_model=CategoryResponseSchema)
async def update_category(category_id: int, updated_category_data: CategoryUpdateSchema, db: AsyncSession = Depends(get_db)):
    return await edit_category(category_id, updated_category_data, db)

@categories_router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    return await remove_category(category_id, db)