from pydantic import BaseModel, Field, ConfigDict, field_serializer

from datetime import datetime

from categories.schemas import CategoryResponseSchema


class TaskORMSchema(BaseModel):
    ''' Basic pydantic schema with model_config '''
    model_config = ConfigDict(from_attributes=True)

class TaskResponseSchema(TaskORMSchema):
    id: int
    title: str
    description: str | None
    status: bool
    category: CategoryResponseSchema
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime, _info):
        return value.strftime('%d.%m.%Y %H:%M')

class TaskCreateSchema(BaseModel):
    title: str = Field(max_length=255)
    description: str | None = Field(default=None)
    category_id: int

class TaskUpdateSchema(BaseModel):
    title: str | None = Field(max_length=255, default=None)
    description: str | None = Field(default=None)
    status: bool | None = Field(default=None)
    category_id: int | None = Field(default=None)