from pydantic import BaseModel, EmailStr
from datetime import datetime
import uuid


# --------------------------
# Output / Response schema
# --------------------------
class AuthorRead(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr | None = None
    user_id: uuid.UUID | None = None
    created_at: datetime

    class Config:
        from_attributes = True


# --------------------------
# Input / Create schema
# --------------------------
class AuthorCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    user_id: uuid.UUID


# --------------------------
# Input / Update schema
# --------------------------
class AuthorUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
