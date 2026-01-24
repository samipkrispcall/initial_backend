from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid


# --------------------------
# Output / Response schema
# --------------------------
class BookRead(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str] = None
    published_at: Optional[datetime] = None
    price: float
    author_id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True


# --------------------------
# Input / Create schema
# --------------------------
class BookCreate(BaseModel):
    title: str
    description: Optional[str] = None
    published_at: Optional[datetime] = None
    price: float = Field(default=0.0, ge=0)
    author_id: uuid.UUID


# --------------------------
# Input / Update schema
# --------------------------
class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    published_at: Optional[datetime] = None
    price: Optional[float] = Field(default=None, ge=0)