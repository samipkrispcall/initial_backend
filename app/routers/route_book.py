from starlette.requests import Request
from starlette.responses import JSONResponse

from app.repositories.repo_book import BookRepository
from app.schemas import schema_book
from app.models.model_book import Book

import uuid


# --------------------------
# GET all books by author_id
# --------------------------
async def get_books(request: Request):
    try:
        author_id = uuid.UUID(request.path_params["author_id"])
        session = request.state.session
        repo = BookRepository(session)
        books = await repo.get_all_by_author_id(author_id)
        books_data = [schema_book.BookRead.from_orm(b).model_dump(mode="json") for b in books]
        return JSONResponse(books_data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# POST new book
# --------------------------
async def create_book(request: Request):
    try:
        data = await request.json()
        book_in = schema_book.BookCreate(**data)
        session = request.state.session
        repo = BookRepository(session)
        book_data = book_in.model_dump()
        book = Book(**book_data)
        book = await repo.create(book)
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
        session = request.state.session
        repo = BookRepository(session)
        book = await repo.get_by_id_and_author_id(book_id, author_id)
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
        data = await request.json()
        book_in = schema_book.BookUpdate(**data)
        session = request.state.session
        repo = BookRepository(session)
        updated = await repo.update(book_id, author_id, book_in.dict(exclude_unset=True))
        if not updated:
            return JSONResponse({"error": "Book not found"}, status_code=404)
        return JSONResponse(schema_book.BookRead.from_orm(updated).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# DELETE book
# --------------------------
async def delete_book(request: Request):
    try:
        author_id = uuid.UUID(request.path_params["author_id"])
        book_id = uuid.UUID(request.path_params["book_id"])
        session = request.state.session
        repo = BookRepository(session)
        deleted = await repo.delete(book_id, author_id)
        if not deleted:
            return JSONResponse({"error": "Book not found"}, status_code=404)
        return JSONResponse({"status": "deleted"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)