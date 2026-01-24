from starlette.routing import Route
from app.routers import route_book


routes = [
    Route("/{author_id}/books", route_book.get_books, methods=["GET"]),
    Route("/books", route_book.create_book, methods=["POST"]),
    Route("/{author_id}/books/{book_id}", route_book.get_book, methods=["GET"]),
    Route("/{author_id}/books/{book_id}", route_book.update_book, methods=["PUT", "PATCH"]),
    Route("/{author_id}/books/{book_id}", route_book.delete_book, methods=["DELETE"]),
]
