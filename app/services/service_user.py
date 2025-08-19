import uuid

# from app.repositories.sql_repo.repo_user import UserRepository
from app.repositories.mongodb_repo.repo_user import UserRepository
from app.schemas.pydantic_schemas.schema_user import UserCreate, UserUpdate


class UserService:
    def __init__(self, session):
        self.repo = UserRepository(session)

    async def get_all_users(self):
        return await self.repo.get_all()

    async def get_user_by_id(self, user_id: uuid.UUID):
        return await self.repo.get_by_id(user_id)

    async def create_user(self, user_in: UserCreate):
        return await self.repo.create(user_in.model_dump())

    async def update_user(self, user_id: uuid.UUID, user_in: UserUpdate):
        return await self.repo.update(user_id, user_in.dict(exclude_unset=True))

    async def delete_user(self, user_id: uuid.UUID) -> bool:
        return await self.repo.delete(user_id)
