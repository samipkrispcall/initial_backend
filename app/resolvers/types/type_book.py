from ariadne import ObjectType
from app.services.sql_services.service_author import AuthorService


class BookTypeResolver:
    def __init__(self):
        self.type = ObjectType("Book")
        self.bind_fields()

    def bind_fields(self):
        self.type.set_field("author", self.resolve_author)

    async def resolve_author(self, book, info):
        session = info.context["session"]
        author_service = AuthorService(session)
        return await author_service.get_author_by_id(book.author_id)
