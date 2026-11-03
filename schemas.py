from pydantic import ConfigDict, BaseModel, EmailStr
from datetime import datetime
import uuid

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)