from select import select

from core.base_dao import BaseDAO
from core.db import async_session_maker

from notes.models import ShortNotes, Categories


class ShortNotesDAO(BaseDAO):
    model = ShortNotes

    @classmethod
    async def find_all_by_category(cls, category_id):
        async with async_session_maker() as session:
            print(cls.model, dir(cls.model))
            category = CategoriesDAO.find_by_id(model_id=category_id)
            query = select(cls.model).filter_by(category=category)
            result = await session.execute(query)
            return result.scalars().all()


class CategoriesDAO(BaseDAO):
    model = Categories
