from src.database import BaseModel

from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(128), unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    tasks = relationship("TaskModel", back_populates="category")