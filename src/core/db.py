from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from settings import settings
from core.logger_wrapper import LoggerWrapper

logger = LoggerWrapper(__name__)

engine = create_async_engine(url=settings.DATABASE_URL, echo=settings.DB_ECHO)
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False,)


class Base(DeclarativeBase):
    pass
