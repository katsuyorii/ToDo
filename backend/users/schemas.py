from pydantic import BaseModel, ConfigDict, field_serializer, field_validator, EmailStr

from datetime import datetime

from .models import UserRoleEnum
from .validators import validation_password


class UserORMSchema(BaseModel):
    ''' Basic pydantic schema with model_config '''
    model_config = ConfigDict(from_attributes=True)

class UserResponseSchema(UserORMSchema):
    email: str
    last_name: str | None
    first_name: str | None
    role: UserRoleEnum
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime, _info):
        return value.strftime('%d.%m.%Y %H:%M')

class UserRegistrationSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def validate_user_password(cls, value: str) -> str:
        return validation_password(value)

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str