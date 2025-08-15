from sqlalchemy import Column, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from datetime import datetime
import uuid

from app.models.sql_models.base import Base


class Book(Base):
    __tablename__ = "books"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(250), nullable=False, index=True)
    description = Column(Text)
    published_at = Column(DateTime, default=datetime.utcnow)
    price = Column(Float, default=0.0, nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    book_author = relationship("Author", back_populates="author_books")
