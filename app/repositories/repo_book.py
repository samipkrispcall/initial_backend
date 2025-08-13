from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.models.model_book import Book

import uuid


class BookRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_author_id(self, author_id: uuid.UUID) -> List[Book]:
        result = await self.session.execute(
            select(Book).where(Book.author_id == author_id)
        )
        return result.scalars().all()

    async def get_by_id_and_author_id(self, book_id: uuid.UUID, author_id: uuid.UUID) -> Optional[Book]:
        result = await self.session.execute(
            select(Book).where(Book.id == book_id, Book.author_id == author_id)
        )
        return result.scalars().first()

    async def create(self, book: Book) -> Book:
        self.session.add(book)
        await self.session.commit()
        await self.session.refresh(book)
        return book

    async def update(self, book_id: uuid.UUID, author_id: uuid.UUID, data: dict) -> Optional[Book]:
        await self.session.execute(
            update(Book)
            .where(Book.id == book_id, Book.author_id == author_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        await self.session.commit()
        return await self.get_by_id_and_author_id(book_id, author_id)

    async def delete(self, book_id: uuid.UUID, author_id: uuid.UUID) -> bool:
        result = await self.session.execute(
            delete(Book).where(Book.id == book_id, Book.author_id == author_id)
        )
        await self.session.commit()
        return result.rowcount > 0