import bcrypt

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from users.models import UserModel


async def hashing_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password.decode()

async def is_email_exists(email: str, db: AsyncSession) -> UserModel | None:
    user = await db.execute(select(UserModel).where(UserModel.email == email))
    return user.scalar_one_or_none()