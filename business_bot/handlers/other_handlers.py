from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command(commands="start"))
async def get_start(message: Message):
    """Срабатывает при команде /start"""
    await message.answer(text="Пивет. Я бот для живого общения. И я почти живой!")


@router.message(Command(commands="help"))
async def get_help(message: Message):
    """Срабатывает при команде /help"""
    await message.answer(text="Просто начни общаться со мной как с живым человеком!")


@router.message(Command(commands="reset"))
async def get_reset(message: Message):
    """Срабатывает при команде /reset"""
    await message.answer(text="Предыдущие сообщения удалены из памяти бота.")
