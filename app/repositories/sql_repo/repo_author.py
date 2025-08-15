from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.models.sql_models.model_author import Author

import uuid


class AuthorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_user_id(self, user_id: uuid.UUID) -> List[Author]:
        result = await self.session.execute(
            select(Author).where(Author.user_id == user_id)
        )
        return result.scalars().all()

    async def get_by_id(self, author_id: uuid.UUID) -> Optional[Author]:
        result = await self.session.execute(
            select(Author).where(Author.id == author_id)
        )
        return result.scalars().first()

    async def get_by_id_and_user_id(self, author_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Author]:
        result = await self.session.execute(
            select(Author).where(Author.id == author_id, Author.user_id == user_id)
        )
        return result.scalars().first()

    async def create(self, author: Author) -> Author:
        self.session.add(author)
        await self.session.commit()
        await self.session.refresh(author)
        return author

    async def update(self, author_id: uuid.UUID, user_id: uuid.UUID, data: dict) -> Optional[Author]:
        await self.session.execute(
            update(Author)
            .where(Author.id == author_id, Author.user_id == user_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        await self.session.commit()
        return await self.get_by_id_and_user_id(author_id, user_id)

    async def delete(self, author_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        author = await self.session.scalar(select(Author).where(Author.id == author_id, Author.user_id == user_id))
        if not author:
            return False
        await self.session.delete(author)
        await self.session.commit()
        return True
