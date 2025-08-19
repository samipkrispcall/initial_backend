import os
import motor.motor_asyncio
from dotenv import load_dotenv
from beanie import init_beanie

from app.models.mongodb_models import \
    UserModel, AuthorModel, BookModel

load_dotenv()


MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL not provided")

client: motor.motor_asyncio.AsyncIOMotorClient | None = None
db = None

async def connect_mongo():
    global client, db
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
    db = client["test-db"]

    # Initialize Beanie with your models
    await init_beanie(
        database=db,
        document_models=[
            UserModel,
            AuthorModel,
            BookModel
        ]
    )

async def close_mongo():
    global client
    if client:
        client.close()
