import uuid
from typing import List, Optional

from app.repositories.sql_repo.repo_book import BookRepository
from app.schemas.pydantic_schemas.schema_book import BookCreate, BookUpdate
from app.models.sql_models.model_book import Book


class BookService:
    def __init__(self, session):
        self.repo = BookRepository(session)

    async def get_books_by_author_id(self, author_id: uuid.UUID) -> List[Book]:
        return await self.repo.get_all_by_author_id(author_id)

    async def get_book_by_id_and_author(self, book_id: uuid.UUID, author_id: uuid.UUID) -> Optional[Book]:
        return await self.repo.get_by_id_and_author_id(book_id, author_id)

    async def create_book(self, book_in: BookCreate) -> Book:
        book = Book(**book_in.model_dump())
        return await self.repo.create(book)

    async def update_book(self, book_id: uuid.UUID, author_id: uuid.UUID, book_in: BookUpdate) -> Optional[Book]:
        return await self.repo.update(book_id, author_id, book_in.dict(exclude_unset=True))

    async def delete_book(self, book_id: uuid.UUID, author_id: uuid.UUID) -> bool:
        return await self.repo.delete(book_id, author_id)
