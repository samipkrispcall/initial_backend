import uuid
from typing import List, Optional

from app.repositories.sql_repo.repo_author import AuthorRepository
from app.schemas.pydantic_schemas.schema_author import AuthorCreate, AuthorUpdate
from app.models.sql_models.model_author import Author


class AuthorService:
    def __init__(self, session):
        self.repo = AuthorRepository(session)

    async def get_authors_by_user_id(self, user_id: uuid.UUID) -> List[Author]:
        return await self.repo.get_all_by_user_id(user_id)

    async def get_author_by_id(self, author_id: uuid.UUID) -> Optional[Author]:
        return await self.repo.get_by_id(author_id)

    async def get_author_by_id_and_user(self, author_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Author]:
        return await self.repo.get_by_id_and_user_id(author_id, user_id)

    async def create_author(self, author_in: AuthorCreate) -> Author:
        author = Author(**author_in.model_dump())
        return await self.repo.create(author)

    async def update_author(self, author_id: uuid.UUID, user_id: uuid.UUID, author_in: AuthorUpdate) -> Optional[Author]:
        return await self.repo.update(author_id, user_id, author_in.dict(exclude_unset=True))

    async def delete_author(self, author_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        return await self.repo.delete(author_id, user_id)
