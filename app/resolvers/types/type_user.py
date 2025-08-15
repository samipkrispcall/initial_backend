from ariadne import ObjectType
from app.services.sql_services.service_author import AuthorService

class UserTypeResolver:
    def __init__(self):
        self.type = ObjectType("User")
        self.bind_fields()

    def bind_fields(self):
        self.type.set_field("authors", self.resolve_authors)

    async def resolve_authors(self, user, info):
        session = info.context["session"]
        author_service = AuthorService(session)
        return await author_service.get_authors_by_user_id(user.id)
