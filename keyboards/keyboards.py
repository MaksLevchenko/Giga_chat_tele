from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_BUTTONS


# Добавление клавиатуры
def add_keyboard(
    width: int, *args: str | tuple[str], **kwargs: str
) -> InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            if type(button) is tuple:
                for text, callback in LEXICON_BUTTONS.items():
                    if text in button[0]:
                        buttons.append(
                            InlineKeyboardButton(
                                text=button[0], callback_data=callback + button[1]
                            )
                        )
            else:
                for text, callback in LEXICON_BUTTONS.items():
                    if button in text:

                        buttons.append(
                            InlineKeyboardButton(text=button, callback_data=callback)
                        )
    if kwargs:
        for callback, text in kwargs.items():
            for t, c in LEXICON_BUTTONS.items():
                if text in t:
                    buttons.append(
                        InlineKeyboardButton(text=text, callback_data=c + callback)
                    )

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()
