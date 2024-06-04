from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import settings

# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/test_marketplace"
engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)