from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.config.sql_db import get_db


class SQLDBSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        async with get_db() as session:
            request.state.session = session
            try:
                response: Response = await call_next(request)
            finally:
                await session.close()
        return response
