import uuid
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.services.sql_services.service_user import UserService
from app.schemas.pydantic_schemas.schema_user import UserCreate, UserUpdate, UserRead


# --------------------------
# GET all users
# --------------------------
async def get_users(request: Request):
    try:
        service = UserService(request.state.session)
        users = await service.get_all_users()
        data = [UserRead.from_orm(u).model_dump(mode="json") for u in users]
        return JSONResponse(data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# POST new user
# --------------------------
async def create_user(request: Request):
    try:
        payload = await request.json()
        user_in = UserCreate(**payload)

        service = UserService(request.state.session)
        user = await service.create_user(user_in)

        return JSONResponse(UserRead.from_orm(user).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# GET user by id
# --------------------------
async def get_user(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        service = UserService(request.state.session)
        user = await service.get_user_by_id(user_id)

        if not user:
            return JSONResponse({"error": "User not found"}, status_code=404)

        return JSONResponse(UserRead.from_orm(user).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# PUT / PATCH update user
# --------------------------
async def update_user(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        payload = await request.json()
        user_in = UserUpdate(**payload)

        service = UserService(request.state.session)
        updated_user = await service.update_user(user_id, user_in)

        if not updated_user:
            return JSONResponse({"error": "User not found"}, status_code=404)

        return JSONResponse(UserRead.from_orm(updated_user).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# DELETE user
# --------------------------
async def delete_user(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        service = UserService(request.state.session)

        deleted = await service.delete_user(user_id)
        if not deleted:
            return JSONResponse({"error": "User not found"}, status_code=404)

        return JSONResponse({"status": "deleted"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
