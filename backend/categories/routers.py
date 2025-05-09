from fastapi import APIRouter, Depends

from src.dependencies import get_db

from sqlalchemy.ext.asyncio import AsyncSession


categories_router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
)

@categories_router.get('/')
async def get_categories(db: AsyncSession = Depends(get_db)):
    return {'message': 'OK'}