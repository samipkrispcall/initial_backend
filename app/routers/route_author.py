import uuid
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.services.restapi_services.service_author import AuthorService
from app.schemas.restapi_schemas import schema_author


# --------------------------
# GET all authors by user_id
# --------------------------
async def get_authors(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        service = AuthorService(request.state.session)

        authors = await service.get_authors_by_user_id(user_id)
        data = [schema_author.AuthorRead.from_orm(a).model_dump(mode="json") for a in authors]

        return JSONResponse(data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# POST new author
# --------------------------
async def create_author(request: Request):
    try:
        payload = await request.json()
        author_in = schema_author.AuthorCreate(**payload)

        service = AuthorService(request.state.session)
        author = await service.create_author(author_in)

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

        service = AuthorService(request.state.session)
        author = await service.get_author_by_id_and_user(author_id, user_id)

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

        payload = await request.json()
        author_in = schema_author.AuthorUpdate(**payload)

        service = AuthorService(request.state.session)
        updated_author = await service.update_author(author_id, user_id, author_in)

        if not updated_author:
            return JSONResponse({"error": "Author not found"}, status_code=404)

        return JSONResponse(schema_author.AuthorRead.from_orm(updated_author).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# DELETE author
# --------------------------
async def delete_author(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        author_id = uuid.UUID(request.path_params["author_id"])

        service = AuthorService(request.state.session)
        deleted = await service.delete_author(author_id, user_id)

        if not deleted:
            return JSONResponse({"error": "Author not found"}, status_code=404)

        return JSONResponse({"status": "deleted"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
