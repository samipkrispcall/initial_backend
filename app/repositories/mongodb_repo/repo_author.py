from typing import List, Optional
import uuid

from app.models.mongodb_models import AuthorModel


class AuthorRepository:
    def __init__(self, session):
        pass

    async def get_all_by_user_id(self, user_id: uuid.UUID) -> List[AuthorModel]:
        return await AuthorModel.find(AuthorModel.user_id == user_id).to_list()

    async def get_by_id(self, author_id: uuid.UUID) -> Optional[AuthorModel]:
        return await AuthorModel.get(author_id)

    async def get_by_id_and_user_id(self, author_id: uuid.UUID, user_id: uuid.UUID) -> Optional[AuthorModel]:
        return await AuthorModel.find_one(AuthorModel.id == author_id, AuthorModel.user_id == user_id)

    async def create(self, data: dict) -> AuthorModel:
        author = AuthorModel(**data)
        await author.insert()
        return author

    async def update(self, author_id: uuid.UUID, user_id: uuid.UUID, data: dict) -> Optional[AuthorModel]:
        author = await self.get_by_id_and_user_id(author_id, user_id)
        if not author:
            return None
        await author.set(data)
        return author

    async def delete(self, author_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        author = await self.get_by_id_and_user_id(author_id, user_id)
        if not author:
            return False
        await author.delete()
        return True
