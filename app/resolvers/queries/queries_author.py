from app.services.service_author import AuthorService


class AuthorQueryResolver:
    def service(self, info):
        session = info.context["session"]
        return AuthorService(session)

    async def resolve_get_author(self, _, info, id):
        return await self.service(info).get_author_by_id(id)

    async def resolve_get_all_authors(self, _, info):
        return await self.service(info).get_all_authors()
