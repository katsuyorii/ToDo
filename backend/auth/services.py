from sqlalchemy.ext.asyncio import AsyncSession

from .utils import hashing_password, is_email_exists
from .exceptions import EMAIL_ALREADY_REGISTERED

from users.models import UserModel
from users.schemas import UserRegistrationSchema


async def registration(user_data: UserRegistrationSchema, db: AsyncSession) -> None:
    user = await is_email_exists(user_data.email, db)

    if user is not None:
        raise EMAIL_ALREADY_REGISTERED

    user_data_dict = user_data.model_dump()

    user_data_dict['password'] = await hashing_password(user_data_dict.get('password'))

    new_user = UserModel(**user_data_dict)

    db.add(new_user)
    await db.commit()