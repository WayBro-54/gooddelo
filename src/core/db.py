from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declared_attr

from src.settings import settings


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


engine = create_async_engine(
    settings.database_url,
)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
)


async def get_async_session():
    async with AsyncSession() as async_session:
        yield async_session
