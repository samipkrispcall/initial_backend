from beanie import Document
from pydantic import Field
from datetime import datetime
from typing import Optional
import uuid

class BookModel(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    description: Optional[str] = None
    published_at: Optional[datetime] = None
    price: float = 0.0
    author_id: uuid.UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "books"
