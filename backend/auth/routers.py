from fastapi import APIRouter, Depends, status

from users.schemas import UserRegistrationSchema

from src.dependencies import get_db

from sqlalchemy.ext.asyncio import AsyncSession

from .services import registration


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)

@auth_router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration_user(user_data: UserRegistrationSchema, db: AsyncSession = Depends(get_db)):
    await registration(user_data, db)
    return {'message': 'Пользователь успешно зарегестрирован!'}