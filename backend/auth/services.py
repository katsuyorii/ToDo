from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession

from .utils import hashing_password, get_user_by_email, verify_password, create_access_token
from .exceptions import EMAIL_ALREADY_REGISTERED, INCORRECT_EMAIL_OR_PASSWORD
from .schemas import JWTTokenSchema

from users.models import UserModel
from users.schemas import UserRegistrationSchema, UserLoginSchema

from src.config import settings


async def registration(user_data: UserRegistrationSchema, db: AsyncSession) -> None:
    user = await get_user_by_email(user_data.email, db)

    if user is not None:
        raise EMAIL_ALREADY_REGISTERED

    user_data_dict = user_data.model_dump()

    user_data_dict['password'] = await hashing_password(user_data_dict.get('password'))

    new_user = UserModel(**user_data_dict)

    db.add(new_user)
    await db.commit()

async def login(user_data: UserLoginSchema, response: Response, db: AsyncSession) -> JWTTokenSchema:
    user = await get_user_by_email(user_data.email, db)

    if not user or not await verify_password(user_data.password, user.password):
        raise INCORRECT_EMAIL_OR_PASSWORD

    access_token = await create_access_token({'sub': user.email})

    response.set_cookie(
        key='access_token',
        value=access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        secure=True,
        httponly=True,
        samesite='strict'
    )

    return JWTTokenSchema(access_token=access_token)