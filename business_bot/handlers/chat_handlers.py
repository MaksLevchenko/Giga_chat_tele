from aiogram import Router
from aiogram.types import Message


from ..gigachat import get_gpt_response


router = Router()


@router.message()
async def fill_link(message: Message):
    """Этот хэндлер будет срабатывать когда начнётся общение"""
    text = get_gpt_response(message.text)
    await message.answer(text=text)
