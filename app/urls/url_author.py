from starlette.routing import Route
from app.routers import route_author


routes = [
    Route("/{user_id}/authors", route_author.get_authors, methods=["GET"]),
    Route("/authors", route_author.create_author, methods=["POST"]),
    Route("/{user_id}/authors/{author_id}", route_author.get_author, methods=["GET"]),
    Route("/{user_id}/authors/{author_id}", route_author.update_author, methods=["PUT", "PATCH"]),
    Route("/{user_id}/authors/{author_id}", route_author.delete_author, methods=["DELETE"]),
]
