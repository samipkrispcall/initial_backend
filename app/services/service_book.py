import uuid

# from app.repositories.sql_repo.repo_book import BookRepository
from app.repositories.mongodb_repo.repo_book import BookRepository
from app.schemas.pydantic_schemas.schema_book import BookCreate, BookUpdate


class BookService:
    def __init__(self, session):
        self.repo = BookRepository(session)

    async def get_books_by_author_id(self, author_id: uuid.UUID):
        return await self.repo.get_all_by_author_id(author_id)

    async def get_book_by_id_and_author(self, book_id: uuid.UUID, author_id: uuid.UUID):
        return await self.repo.get_by_id_and_author_id(book_id, author_id)

    async def create_book(self, book_in: BookCreate):
        return await self.repo.create(book_in.model_dump())

    async def update_book(self, book_id: uuid.UUID, author_id: uuid.UUID, book_in: BookUpdate):
        return await self.repo.update(book_id, author_id, book_in.dict(exclude_unset=True))

    async def delete_book(self, book_id: uuid.UUID, author_id: uuid.UUID) -> bool:
        return await self.repo.delete(book_id, author_id)
