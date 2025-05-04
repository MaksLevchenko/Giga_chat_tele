from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from crud.crud import (
    load_messages_from_db,
    save_messages_to_db,
    clear_message_from_memory_bot,
)
from config.settings import settings
from .models import model


async def get_gpt_response(text: str, user_id: str):
    """Обращается к gigachat и возвращает ответ от нейросети"""

    loaded_records = await load_messages_from_db(
        user_id=user_id
    )  # Загружаем ранее сохранённые сообщения

    style = loaded_records[-1].style if loaded_records else None
    role_bot = loaded_records[-1].role_bot if loaded_records else None

    new_message = HumanMessage(content=text)
    await save_messages_to_db(
        user_id=user_id, message=new_message, style=style, role_bot=role_bot
    )  # Сохраняем сообщение в базу данных

    loaded_messages = [
        {"type": record.role, "content": record.content} for record in loaded_records
    ]
    loaded_messages.append({"type": "human", "content": new_message.content})

    if len(loaded_messages) >= settings.max_messages * 2:
        await clear_message_from_memory_bot(
            user_id=user_id, first_record=loaded_records[0]
        )

    final_messages = [
        (
            SystemMessage(content=f"Ты собеседник который общается в {style} стиле")
            if not role_bot
            else SystemMessage(
                content=f"Ты {role_bot} который общается в {style} стиле"
            )
        )
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
        user_id=user_id, message=AIMessage(res.content), style=style, role_bot=role_bot
    )  # Сохраняем обновлённую историю
    return res.content
