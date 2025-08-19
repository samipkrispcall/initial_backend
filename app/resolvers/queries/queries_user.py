import uuid
from app.services.service_user import UserService

class UserQueryResolver:
    def service(self, info):
        session = info.context["session"]
        return UserService(session)

    async def resolve_get_user(self, _, info, id):
        id = uuid.UUID(id)
        return await self.service(info).get_user_by_id(id)

    async def resolve_get_all_users(self, _, info):
        return await self.service(info).get_all_users()
