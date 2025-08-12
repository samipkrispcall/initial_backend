from starlette.routing import Route
from app import routes


routes = [
    Route("/names", routes.get_names, methods=["GET"]),
    Route("/is_prime", routes.post_is_prime, methods=["POST"]),
]
