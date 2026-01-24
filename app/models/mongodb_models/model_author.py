from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime
import uuid

class AuthorModel(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    email: EmailStr | None = None
    user_id: uuid.UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "authors"
