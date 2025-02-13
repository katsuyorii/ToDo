from sqlalchemy import func, text, String, Text, ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database.database import BaseModel


tasks_tags = Table(
    'tasks_tags',
    BaseModel.metadata,
    Column('task_id', ForeignKey('tasks.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True),
)

class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(128), unique=True)

    tasks = relationship('TaskModel', back_populates='category')

class TagModel(BaseModel):
    __tablename__ = 'tags'

    name: Mapped[str] = mapped_column(String(128), unique=True)

    tasks = relationship('TaskModel', secondary=tasks_tags, back_populates='tags')

class TaskModel(BaseModel):
    __tablename__ = 'tasks'

    title: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(server_default=text('False'))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category = relationship('CategoryModel', back_populates='tasks')
    tags = relationship('TagModel', secondary=tasks_tags, back_populates='tasks')