from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from langchain_core.messages import HumanMessage

from crud.crud import (
    clear_message_from_memory_bot,
    load_messages_from_db,
    save_messages_to_db,
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


@router.message(Command(commands="reset"))
async def get_reset(message: Message):
    """Срабатывает при команде /reset"""
    await clear_message_from_memory_bot(user_id=message.from_user.id, all=True)
    await message.answer(text="Предыдущие сообщения удалены из памяти бота.")


@router.message(Command(commands="style"))
async def get_stule(message: Message, state: FSMContext):
    """Срабатывает при команде /style"""

    markup = add_keyboard(
        2, "Вежливый", "Грубый", "Деловой", "Насмешливый", "Юморной", "Неформальный"
    )
    await message.answer(text="Выберите стиль:", reply_markup=markup)

    await state.set_state(FSMEditStyle.fill_style)


@router.callback_query(StateFilter(FSMEditStyle.fill_style))
async def edit_style(callback: CallbackQuery, state: FSMContext):
    """Срабатывает при смене стиля общения"""

    user_id = callback.from_user.id
    loaded_records = await load_messages_from_db(
        user_id=user_id
    )  # Загружаем ранее сохранённые сообщения

    role_bot = loaded_records[-1].role_bot if loaded_records else None
    await save_messages_to_db(
        user_id=user_id,
        message=HumanMessage(content="Смена стиля общения"),
        style=callback.data,
        role_bot=role_bot,
    )

    await callback.message.answer(text="Стиль успешно сменён")
    await callback.message.delete()
    await state.clear()


@router.message(Command(commands="role"))
async def get_role(message: Message, state: FSMContext):
    """Срабатывает при команде /role"""

    markup = add_keyboard(2, "Психолог", "Друг", "Враг", "Пьяный ковбой")
    await message.answer(text="Выберите роль бота:", reply_markup=markup)

    await state.set_state(FSMEditStyle.fill_role)


@router.callback_query(StateFilter(FSMEditStyle.fill_role))
async def edit_role(callback: CallbackQuery, state: FSMContext):
    """Срабатывает при смене роли бота"""

    user_id = callback.from_user.id

    loaded_records = await load_messages_from_db(
        user_id=user_id
    )  # Загружаем ранее сохранённые сообщения

    style = loaded_records[-1].style if loaded_records else None
    await save_messages_to_db(
        user_id=user_id,
        message=HumanMessage(content="Смена роли бота"),
        style=style,
        role_bot=callback.data,
    )

    await callback.message.answer(text="Роль успешно сменена")
    await callback.message.delete()
    await state.clear()
