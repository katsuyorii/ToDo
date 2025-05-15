from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies import get_db

from users.models import UserModel

from .utils import verify_jwt_token
from .exceptions import INVALID_JWT_TOKEN
from .utils import get_user_by_email


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> UserModel:
    payload = await verify_jwt_token(token)
    email = payload.get('sub')

    if not email:
        raise INVALID_JWT_TOKEN
    
    user = await get_user_by_email(email, db)

    if not user:
        pass

    return user