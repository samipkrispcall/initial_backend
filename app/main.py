from starlette.applications import Starlette
from contextlib import asynccontextmanager

from app.config.db import engine
from app.urls import url_user, url_author, url_book
from app.middlewares import mw_request_logger, mw_db_session


@asynccontextmanager
async def lifespan(app: Starlette):
    yield  # Application runs here
    await engine.dispose()

all_routes = url_user.routes + url_author.routes + url_book.routes

app = Starlette(
    debug=True,
    routes=all_routes,
    lifespan=lifespan
)

app.add_middleware(mw_request_logger.LoggingMiddleware)
app.add_middleware(mw_db_session.DBSessionMiddleware)
