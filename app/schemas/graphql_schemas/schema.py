from ariadne import make_executable_schema, load_schema_from_path, ObjectType
from ariadne.asgi import GraphQL

from app.resolvers.queries.queries import QueryResolver
from app.resolvers.types.types import TypeResolver

# Load SDL from schema.graphql
type_defs = load_schema_from_path("app/schemas/graphql_schemas/schema.graphql")

# Create Query ObjectType and bind resolvers
query = ObjectType("Query")
query_resolver = QueryResolver()
query.set_field("getUser", query_resolver.resolve_get_user)
query.set_field("getAllUsers", query_resolver.resolve_get_all_users)
query.set_field("getAuthor", query_resolver.resolve_get_author)
query.set_field("getAllAuthors", query_resolver.resolve_get_all_authors)
query.set_field("getBook", query_resolver.resolve_get_book)
query.set_field("getAllBooks", query_resolver.resolve_get_all_books)

# Instantiate combined TypeResolver
type_resolver = TypeResolver()

# Create executable schema
schema = make_executable_schema(
    type_defs,
    query,
    type_resolver.user_type.type,
    type_resolver.author_type.type,
    type_resolver.book_type.type
)

# Create ASGI GraphQL app
graphql_app = GraphQL(
    schema,
    debug=True,
    context_value=lambda request: {"session": request.state.session}
)
