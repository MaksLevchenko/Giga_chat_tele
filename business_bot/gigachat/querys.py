from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from crud.crud import load_messages_from_db, save_messages_to_db
from .models import model


async def get_gpt_response(text: str, user_id: int):
    """Обращается к gigachat и возвращает ответ от нейросети"""

    await save_messages_to_db(
        user_id=user_id, messages=[HumanMessage(content=text)]
    )  # Сохраняем историю в базу данных

    loaded_messages = await load_messages_from_db(
        user_id=user_id
    )  # Загружаем ранее сохранённые сообщения
    final_messages = [
        SystemMessage(content="Имитируй обычное человеческое общение")
    ] + [
        (
            HumanMessage(content=msg["content"])
            if msg["type"] == "human"
            else AIMessage(content=msg["content"])
        )
        for msg in loaded_messages
    ]

    res = model.invoke(final_messages)
    await save_messages_to_db(
        user_id=user_id, messages=[AIMessage(res.content)]
    )  # Сохраняем обновлённую историю
    return res.content
