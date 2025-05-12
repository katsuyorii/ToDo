from pydantic import BaseModel, ConfigDict


class CategoryORMSchema(BaseModel):
    ''' Basic pydantic schema with model_config '''
    model_config = ConfigDict(from_attributes=True)

class CategoryResponseSchema(CategoryORMSchema):
    id: int
    name: str