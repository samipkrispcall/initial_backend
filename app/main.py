from starlette.applications import Starlette
from starlette.routing import Route
from contextlib import asynccontextmanager

from app.config.sql_db import engine
from app.config.mongo_db import connect_mongo, close_mongo
from app.schemas.graphql_schemas.schema import graphql_app
from app.urls import url_user, url_author, url_book
from app.middlewares import mw_request_logger, mw_sqldb_session


@asynccontextmanager
async def lifespan(app: Starlette):
    await connect_mongo()
    yield  # Application runs here
    await engine.dispose()
    await close_mongo()

all_routes = url_user.routes + url_author.routes + url_book.routes
all_routes.append(Route("/graphql", graphql_app))

app = Starlette(
    debug=True,
    routes=all_routes,
    lifespan=lifespan
)

app.add_middleware(mw_request_logger.LoggingMiddleware)
app.add_middleware(mw_sqldb_session.SQLDBSessionMiddleware)
