from typing import List, Optional
import uuid

from app.models.mongodb_models import UserModel


class UserRepository:
    def __init__(self, session):
        pass

    async def get_all(self) -> List[UserModel]:
        return await UserModel.find_all().to_list()

    async def get_by_id(self, user_id: uuid.UUID) -> Optional[UserModel]:
        return await UserModel.get(user_id)

    async def create(self, data: dict) -> UserModel:
        user = UserModel(**data)
        await user.insert()
        return user

    async def update(self, user_id: uuid.UUID, data: dict) -> Optional[UserModel]:
        user = await UserModel.get(user_id)
        if not user:
            return None
        await user.set(data)
        return user

    async def delete(self, user_id: uuid.UUID) -> bool:
        user = await UserModel.get(user_id)
        if not user:
            return False
        await user.delete()
        return True
