from app.resolvers.queries.queries_user import UserQueryResolver
from app.resolvers.queries.queries_author import AuthorQueryResolver
from app.resolvers.queries.queries_book import BookQueryResolver


class QueryResolver(
    UserQueryResolver,
    AuthorQueryResolver,
    BookQueryResolver
):
    def __init__(self):
        UserQueryResolver.__init__(self)
        AuthorQueryResolver.__init__(self)
        BookQueryResolver.__init__(self)
