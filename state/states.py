from aiogram.fsm.state import State, StatesGroup


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMEditStyle(StatesGroup):
    fill_style = State()  # Состояние ожидания нового стиля
    fill_role = State()  # Состояние ожидания новой роли
    fill_custom_role = State()  # Состояние ожидания ввода новой роли
    fill_custom_style = State()  # Состояние ожидания ввода нового стиля
