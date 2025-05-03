from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command(commands="start"))
async def get_start(message: Message):
    print(message.bot.context)
    await message.answer(text="start")
