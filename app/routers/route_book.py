import uuid
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.services.restapi_services.service_book import BookService
from app.schemas.restapi_schemas import schema_book


# --------------------------
# GET all books by author_id
# --------------------------
async def get_books(request: Request):
    try:
        author_id = uuid.UUID(request.path_params["author_id"])
        service = BookService(request.state.session)

        books = await service.get_books_by_author_id(author_id)
        data = [schema_book.BookRead.from_orm(b).model_dump(mode="json") for b in books]

        return JSONResponse(data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# POST new book
# --------------------------
async def create_book(request: Request):
    try:
        payload = await request.json()
        book_in = schema_book.BookCreate(**payload)

        service = BookService(request.state.session)
        book = await service.create_book(book_in)

        return JSONResponse(schema_book.BookRead.from_orm(book).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# GET book by id and author_id
# --------------------------
async def get_book(request: Request):
    try:
        author_id = uuid.UUID(request.path_params["author_id"])
        book_id = uuid.UUID(request.path_params["book_id"])

        service = BookService(request.state.session)
        book = await service.get_book_by_id_and_author(book_id, author_id)

        if not book:
            return JSONResponse({"error": "Book not found"}, status_code=404)

        return JSONResponse(schema_book.BookRead.from_orm(book).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# PUT / PATCH update book
# --------------------------
async def update_book(request: Request):
    try:
        author_id = uuid.UUID(request.path_params["author_id"])
        book_id = uuid.UUID(request.path_params["book_id"])

        payload = await request.json()
        book_in = schema_book.BookUpdate(**payload)

        service = BookService(request.state.session)
        updated_book = await service.update_book(book_id, author_id, book_in)

        if not updated_book:
            return JSONResponse({"error": "Book not found"}, status_code=404)

        return JSONResponse(schema_book.BookRead.from_orm(updated_book).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# DELETE book
# --------------------------
async def delete_book(request: Request):
    try:
        author_id = uuid.UUID(request.path_params["author_id"])
        book_id = uuid.UUID(request.path_params["book_id"])

        service = BookService(request.state.session)
        deleted = await service.delete_book(book_id, author_id)

        if not deleted:
            return JSONResponse({"error": "Book not found"}, status_code=404)

        return JSONResponse({"status": "deleted"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
