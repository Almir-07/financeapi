from pydantic import ConfigDict, BaseModel, EmailStr,Field
from datetime import datetime
import uuid

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8,max_length=128)
    full_name: str = Field(min_length=1)

class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str 
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)