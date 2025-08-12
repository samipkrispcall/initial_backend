from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from app.repository import InMemoryPersonRepository
from app.services import is_prime

import json


person_repo = InMemoryPersonRepository()


async def get_names(request: Request):
    names = await person_repo.list_names()
    return JSONResponse({"names": names}, status_code=HTTP_200_OK)


async def post_is_prime(request: Request):
    try:
        data = await request.json()
        number = data.get("number")
        if not isinstance(number, int) or number <= 0:
            raise ValueError
    except (json.JSONDecodeError, ValueError, AttributeError):
        return JSONResponse(
            {"error": "'number' field is required and must be a positive integer"},
            status_code=HTTP_400_BAD_REQUEST)

    result = is_prime(number)
    return JSONResponse({"is_prime": result}, status_code=HTTP_200_OK)
