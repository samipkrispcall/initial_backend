from typing import List, Optional
import uuid

from app.models.mongodb_models import BookModel


class BookRepository:
    def __init__(self, session):
        pass

    async def get_all_by_author_id(self, author_id: uuid.UUID) -> List[BookModel]:
        return await BookModel.find(BookModel.author_id == author_id).to_list()

    async def get_by_id_and_author_id(self, book_id: uuid.UUID, author_id: uuid.UUID) -> Optional[BookModel]:
        return await BookModel.find_one(BookModel.id == book_id, BookModel.author_id == author_id)

    async def create(self, data: dict) -> BookModel:
        book = BookModel(**data)
        await book.insert()
        return book

    async def update(self, book_id: uuid.UUID, author_id: uuid.UUID, data: dict) -> Optional[BookModel]:
        book = await self.get_by_id_and_author_id(book_id, author_id)
        if not book:
            return None
        await book.set(data)
        return book

    async def delete(self, book_id: uuid.UUID, author_id: uuid.UUID) -> bool:
        book = await self.get_by_id_and_author_id(book_id, author_id)
        if not book:
            return False
        await book.delete()
        return True
