from pydantic import BaseModel, Field, ConfigDict, field_serializer

from datetime import datetime


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: bool
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime, _info):
        return value.strftime('%d.%m.%Y %H:%M')

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    title: str = Field(max_length=255)
    description: str | None = Field(default=None)