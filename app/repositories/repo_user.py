from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.models.model_user import User
from app.models.base import pwd_context

import uuid


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[User]:
        result = await self.session.execute(select(User))
        return result.scalars().all()

    async def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    async def create(self, user: User) -> User:
        user.set_password(user.password)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update(self, user_id: uuid.UUID, data: dict) -> Optional[User]:
        if "password" in data:
            data["password"] = pwd_context.hash(data["password"])
        await self.session.execute(
            update(User)
            .where(User.id == user_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        await self.session.commit()
        return await self.get_by_id(user_id)

    async def delete(self, user_id: uuid.UUID) -> bool:
        result = await self.session.execute(delete(User).where(User.id == user_id))
        await self.session.commit()
        return result.rowcount > 0
