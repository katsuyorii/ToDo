from src.database import BaseModel

from enum import Enum

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class UserRoleEnum(str, Enum):
    USER = 'user'
    ADMIN = 'admin'

class UserModel(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[UserRoleEnum] = mapped_column(default=UserRoleEnum.USER)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())