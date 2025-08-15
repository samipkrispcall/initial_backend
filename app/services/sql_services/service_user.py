import uuid
from typing import List, Optional

from app.repositories.sql_repo.repo_user import UserRepository
from app.schemas.pydantic_schemas.schema_user import UserCreate, UserUpdate
from app.models.sql_models.model_user import User


class UserService:
    def __init__(self, session):
        self.repo = UserRepository(session)

    async def get_all_users(self) -> List[User]:
        return await self.repo.get_all()

    async def get_user_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        return await self.repo.get_by_id(user_id)

    async def create_user(self, user_in: UserCreate) -> User:
        user = User(**user_in.model_dump())
        return await self.repo.create(user)

    async def update_user(self, user_id: uuid.UUID, user_in: UserUpdate) -> Optional[User]:
        return await self.repo.update(user_id, user_in.dict(exclude_unset=True))

    async def delete_user(self, user_id: uuid.UUID) -> bool:
        return await self.repo.delete(user_id)
