from starlette.applications import Starlette

from app.urls import routes
from app.middleware import LoggingMiddleware


app = Starlette(debug=True, routes=routes)

app.add_middleware(LoggingMiddleware)
