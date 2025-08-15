from ariadne import ObjectType
from app.services.sql_services.service_user import UserService
from app.services.sql_services.service_book import BookService


class AuthorTypeResolver:
    def __init__(self):
        self.type = ObjectType("Author")
        self.bind_fields()

    def bind_fields(self):
        self.type.set_field("user", self.resolve_user)
        self.type.set_field("books", self.resolve_books)

    async def resolve_user(self, author, info):
        session = info.context["session"]
        user_service = UserService(session)
        return await user_service.get_user_by_id(author.user_id)

    async def resolve_books(self, author, info):
        session = info.context["session"]
        book_service = BookService(session)
        return await book_service.get_books_by_author_id(author.id)
 