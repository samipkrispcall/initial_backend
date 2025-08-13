from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from app.repositories.repo_user import UserRepository
from app.schemas import schema_user
from app.models import User

import uuid


# --------------------------
# GET all users
# --------------------------
async def get_users(request: Request):
    try:
        session = request.state.session
        repo = UserRepository(session)
        users = await repo.get_all()
        users_data = [schema_user.UserRead.from_orm(u).model_dump(mode="json") for u in users]
        return JSONResponse(users_data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# POST new user
# --------------------------
async def create_user(request: Request):
    try:
        data = await request.json()
        user_in = schema_user.UserCreate(**data)
        session = request.state.session
        repo = UserRepository(session)
        user_data = user_in.model_dump()
        user = User(**user_data)
        user = await repo.create(user)
        return JSONResponse(schema_user.UserRead.from_orm(user).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# GET user by id
# --------------------------
async def get_user(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        session = request.state.session
        repo = UserRepository(session)
        user = await repo.get_by_id(user_id)
        if not user:
            return JSONResponse({"error": "User not found"}, status_code=404)
        return JSONResponse(schema_user.UserRead.from_orm(user).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# PUT / PATCH update user
# --------------------------
async def update_user(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        data = await request.json()
        user_in = schema_user.UserUpdate(**data)
        session = request.state.session
        repo = UserRepository(session)
        updated = await repo.update(user_id, user_in.dict(exclude_unset=True))
        if not updated:
            return JSONResponse({"error": "User not found"}, status_code=404)
        return JSONResponse(schema_user.UserRead.from_orm(updated).model_dump(mode="json"))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# --------------------------
# DELETE user
# --------------------------
async def delete_user(request: Request):
    try:
        user_id = uuid.UUID(request.path_params["user_id"])
        session = request.state.session
        repo = UserRepository(session)
        deleted = await repo.delete(user_id)
        if not deleted:
            return JSONResponse({"error": "User not found"}, status_code=404)
        return JSONResponse({"status": "deleted"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
