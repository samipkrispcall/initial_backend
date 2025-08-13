from pydantic import BaseModel, EmailStr
from datetime import datetime
import uuid


# --------------------------
# Output / Response schema
# --------------------------
class UserRead(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# --------------------------
# Input / Create schema
# --------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# --------------------------
# Input / Update schema
# --------------------------
class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
