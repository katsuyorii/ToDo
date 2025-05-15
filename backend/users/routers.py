from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user

from .schemas import UserResponseSchema
from .models import UserModel


users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

@users_router.get('/me', response_model=UserResponseSchema)
async def get_me(current_user: UserModel = Depends(get_current_user)):
    return current_user