from fastapi import APIRouter, Depends, status, Response

from users.schemas import UserRegistrationSchema, UserLoginSchema

from src.dependencies import get_db

from sqlalchemy.ext.asyncio import AsyncSession

from .services import registration, login
from .schemas import JWTTokenSchema


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)

@auth_router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration_user(user_data: UserRegistrationSchema, db: AsyncSession = Depends(get_db)):
    await registration(user_data, db)
    return {'message': 'Пользователь успешно зарегестрирован!'}

@auth_router.post('/login', response_model=JWTTokenSchema)
async def login_user(user_data: UserLoginSchema, response: Response, db: AsyncSession = Depends(get_db)):
    return await login(user_data, response, db)

@auth_router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('access_token')
    
    return {'message': 'Вы успешно вышли из системы!'}