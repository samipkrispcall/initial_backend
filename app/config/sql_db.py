import os
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL_ASYNC = os.getenv("DATABASE_URL_ASYNC")
if not DATABASE_URL_ASYNC:
    raise ValueError("DATABASE_URL_ASYNC is not provided")

# Async engine
engine = create_async_engine(
    DATABASE_URL_ASYNC,
    echo=False,
    future=True
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

# Dependency-style session getter
@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
