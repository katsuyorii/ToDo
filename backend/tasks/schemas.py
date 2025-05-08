from pydantic import BaseModel, Field

from datetime import datetime


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str = Field(max_length=255)
    description: str | None = Field(default=None)