from starlette.routing import Route
from app.routers import route_user


routes = [
    Route("/users", route_user.get_users, methods=["GET"]),
    Route("/users", route_user.create_user, methods=["POST"]),
    Route("/users/{user_id}", route_user.get_user, methods=["GET"]),
    Route("/users/{user_id}", route_user.update_user, methods=["PUT", "PATCH"]),
    Route("/users/{user_id}", route_user.delete_user, methods=["DELETE"]),
]
