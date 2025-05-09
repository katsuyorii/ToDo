from src.database import BaseModel

from datetime import datetime

from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TaskModel(BaseModel):
    __tablename__ = 'tasks'

    title: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category = relationship("CategoryModel", back_populates="tasks")