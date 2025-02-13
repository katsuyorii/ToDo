from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class CategoryResponseSchema(BaseModel):
    id: int
    name: str

class TagResponseSchema(BaseModel):
    id: int
    name: str

class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime
    category: CategoryResponseSchema
    tags: List[TagResponseSchema]

class CategorySchema(BaseModel):
    name: str = Field(max_length=128)

class TagSchema(BaseModel):
    name: str = Field(max_length=128)

class TaskCreateSchema(BaseModel):
    title: str = Field(max_length=128)
    description: Optional[str] = Field(default=None)
    category_id: int
    tags: List[int]

    class Config:
        from_attributes = True

class TaskEditSchema(TaskCreateSchema):
    is_completed: bool
    
    class Config:
        from_attributes = True