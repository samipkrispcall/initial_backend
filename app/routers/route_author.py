from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from app.repositories.repo_author import AuthorRepository
from app.schemas import schema_author
from app.models.model_author import Author

import uuid


# --------------------------
# GET all authors by user_id
# --------------------------
async def get_authors(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        session = request.state.session
        repo = AuthorRepository(session)
        authors = await repo.get_all_by_user_id(user_id)
        authors_data = [schema_author.AuthorRead.from_orm(a).model_dump(mode="json") for a in authors]
        return JSONResponse(authors_data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# POST new author
# --------------------------
async def create_author(request: Request):
    try:
        data = await request.json()
        author_in = schema_author.AuthorCreate(**data)
        session = request.state.session
        repo = AuthorRepository(session)
        author_data = author_in.model_dump()
        author = Author(**author_data)
        author = await repo.create(author)
        return JSONResponse(schema_author.AuthorRead.from_orm(author).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# GET author by id and user_id
# --------------------------
async def get_author(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        author_id = uuid.UUID(request.path_params["author_id"])
        session = request.state.session
        repo = AuthorRepository(session)
        author = await repo.get_by_id_and_user_id(author_id, user_id)
        if not author:
            return JSONResponse({"error": "Author not found"}, status_code=404)
        return JSONResponse(schema_author.AuthorRead.from_orm(author).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# PUT / PATCH update author
# --------------------------
async def update_author(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        author_id = uuid.UUID(request.path_params["author_id"])
        data = await request.json()
        author_in = schema_author.AuthorUpdate(**data)
        session = request.state.session
        repo = AuthorRepository(session)
        updated = await repo.update(author_id, user_id, author_in.dict(exclude_unset=True))
        if not updated:
            return JSONResponse({"error": "Author not found"}, status_code=404)
        return JSONResponse(schema_author.AuthorRead.from_orm(updated).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# DELETE author
# --------------------------
async def delete_author(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        author_id = uuid.UUID(request.path_params["author_id"])
        session = request.state.session
        repo = AuthorRepository(session)
        deleted = await repo.delete(author_id, user_id)
        if not deleted:
            return JSONResponse({"error": "Author not found"}, status_code=404)
        return JSONResponse({"status": "deleted"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)