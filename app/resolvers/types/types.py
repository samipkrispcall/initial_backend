from app.resolvers.types.type_user import UserTypeResolver
from app.resolvers.types.type_author import AuthorTypeResolver
from app.resolvers.types.type_book import BookTypeResolver


class TypeResolver:
    def __init__(self):
        self.user_type = UserTypeResolver()
        self.author_type = AuthorTypeResolver()
        self.book_type = BookTypeResolver()
