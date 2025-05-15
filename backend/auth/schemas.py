from pydantic import BaseModel, Field


class JWTTokenSchema(BaseModel):
    access_token: str
    type: str = Field(default='Bearer')