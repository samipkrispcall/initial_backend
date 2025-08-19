from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime
import uuid

class UserModel(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
