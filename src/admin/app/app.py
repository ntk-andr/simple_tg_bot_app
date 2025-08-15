from core.db import engine

from fastapi import FastAPI
from sqladmin import Admin, ModelView

from notes.models import Categories, ShortNotes

from notes.router import router as notes_router
from core.logger_wrapper import LoggerWrapper

logger = LoggerWrapper(__name__)

app = FastAPI(debug=True)

admin = Admin(
    app=app,
    engine=engine
)


class ShortNoteAdmin(ModelView, model=ShortNotes):
    name_plural = 'Заметки'
    name = 'Заметка'
    column_list = ['id', 'title', 'category']


class CategoryAdmin(ModelView, model=Categories):
    name_plural = 'Категории'
    name = 'Категория'
    column_list = ['id', 'title']


admin.add_view(CategoryAdmin)
admin.add_view(ShortNoteAdmin)

app.include_router(notes_router)
