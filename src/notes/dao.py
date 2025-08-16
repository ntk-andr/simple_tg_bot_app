from sqlalchemy import select

from core.base_dao import BaseDAO
from core.db import async_session_maker
from core.logger_wrapper import LoggerWrapper
from sqlalchemy.orm import joinedload
from notes.models import ShortNotes, Categories

logger = LoggerWrapper(__name__).logger


class ShortNotesDAO(BaseDAO):
    model = ShortNotes

    @classmethod
    async def find_all_by_category(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.category)).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()


class CategoriesDAO(BaseDAO):
    model = Categories
