import asyncio
import logging
import random
import sys
import traceback

from notes.dao import CategoriesDAO, ShortNotesDAO, Categories
from settings import settings
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup
)

from core.logger_wrapper import LoggerWrapper

logger = LoggerWrapper(__name__).logger

bot = Bot(token=settings.TG_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome_handler(message: Message) -> None:
    try:
        category = await CategoriesDAO.find_one_or_none(title='интро')
        for short_note in await ShortNotesDAO.find_all_by_category(category_id=category.id):
            await message.answer(short_note.text)
            await bot.send_chat_action(message.chat.id, action='typing')
            await asyncio.sleep(random.randint(1, 5))
        else:
            categories = [KeyboardButton(text=category.title) for category in await CategoriesDAO.find_all()]
            await message.answer(
                'а на этом всё) выбирайте `категории`, смотрите `заметки`',
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[categories],
                    resize_keyboard=True,
                ),
            )

    except Exception as e:
        await message.answer(f'Exception {e} {traceback.format_exc()}!')


@dp.message(F.text.in_(['категории', 'заметки']))
async def cats_handler(message: Message) -> None:
    try:
        if message.text == 'заметки':
            for note in await ShortNotesDAO.find_all():
                text = f"{note.title}\n{note.text}"
                reply_markup = None
                await message.answer(
                    text=text,
                    reply_markup=reply_markup
                )
        if message.text == 'категории':
            text = 'Выберите категорию'
            categories = [KeyboardButton(text=category.title) for category in await CategoriesDAO.find_all()]
            reply_markup = ReplyKeyboardMarkup(
                keyboard=[categories],
                resize_keyboard=True,
            )
            await message.answer(
                text=text,
                reply_markup=reply_markup
            )

    except Exception as e:
        await message.answer(f'Exception {e} {traceback.format_exc()}!')


@dp.message()
async def notes_handler(message: Message) -> None:
    try:
        categories_titles = [category.title for category in await CategoriesDAO.find_all()]
        category = await CategoriesDAO.find_one_or_none(title=message.text)
        if message.text in categories_titles:
            for note in await ShortNotesDAO.find_all_by_category(category_id=category.id):
                await message.answer(text=note.text)

    except Exception as e:
        await message.answer(f'упс, что-то пошло не так!')
        logger.error(f'Exception {e} {traceback.format_exc()}!')


async def main() -> None:
    try:
        await dp.start_polling(bot)
    except Exception as te:
        logger.error(te)
