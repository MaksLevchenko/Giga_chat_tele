from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from sqlalchemy.orm import DeclarativeBase

from config.settings import settings


# Base = declarative_base()
class Base(DeclarativeBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)


# Вывод сгенерированных запросов в логи: echo=True
_asyncio_engine = create_async_engine(
    settings.postgres_url, echo=settings.pg_engine_echo
)

pg_async_session = async_sessionmaker(
    bind=_asyncio_engine, autoflush=False, expire_on_commit=False
)
