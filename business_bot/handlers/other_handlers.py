from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from crud.crud import (
    clear_message_from_memory_bot,
)
from keyboards.keyboards import add_keyboard
from state import FSMEditStyle


router = Router()


@router.message(Command(commands="start"))
async def get_start(message: Message):
    """Срабатывает при команде /start"""
    await message.answer(text="Пивет. Я бот для живого общения. И я почти живой!")


@router.message(Command(commands="help"))
async def get_help(message: Message):
    """Срабатывает при команде /help"""
    await message.answer(text="Просто начни общаться со мной как с живым человеком!")


@router.message(Command(commands="about"))
async def get_about(message: Message):
    """Срабатывает при команде /about"""
    await message.answer(
        text="Этот бот предназначен для общения как с живым человеком!\
                          Можно сменить стиль общения бота, а также роль бота, например задать роль психолога или пьяного ковбоя!\
                          Но можно самим придумывать стили и роли бота в общении! Дерзайте!"
    )


@router.message(Command(commands="reset"))
async def get_reset(message: Message):
    """Срабатывает при команде /reset"""
    await clear_message_from_memory_bot(user_id=str(message.from_user.id), all=True)
    await message.answer(text="Предыдущие сообщения удалены из памяти бота.")


@router.message(Command(commands="style"))
async def get_stule(message: Message, state: FSMContext):
    """Срабатывает при команде /style"""

    markup = add_keyboard(
        2,
        "Вежливый",
        "Грубый",
        "Деловой",
        "Насмешливый",
        "Юморной",
        "Неформальный",
        "Своё",
    )
    await message.answer(text="Выберите стиль:", reply_markup=markup)

    await state.set_state(FSMEditStyle.fill_style)


@router.message(Command(commands="role"))
async def get_role(message: Message, state: FSMContext):
    """Срабатывает при команде /role"""

    markup = add_keyboard(2, "Психолог", "Друг", "Враг", "Пьяный ковбой", "Своё")
    await message.answer(text="Выберите роль бота:", reply_markup=markup)

    await state.set_state(FSMEditStyle.fill_role)
