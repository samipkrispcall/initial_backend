from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.models.sql_models.model_book import Book

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

    async def create(self, data: dict) -> Book:
        book = Book(**data)
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
        book = await self.session.scalar(select(Book).where(Book.id == book_id, Book.author_id == author_id))
        if not book:
            return False
        await self.session.delete(book)
        await self.session.commit()
        return True
