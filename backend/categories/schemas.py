from pydantic import BaseModel, Field, ConfigDict


class CategoryORMSchema(BaseModel):
    ''' Basic pydantic schema with model_config '''
    model_config = ConfigDict(from_attributes=True)

class CategoryResponseSchema(CategoryORMSchema):
    id: int
    name: str

class CategoryCreateSchema(BaseModel):
    name: str = Field(max_length=128)

class CategoryUpdateSchema(BaseModel):
    name: str | None = Field(default=None, max_length=128)