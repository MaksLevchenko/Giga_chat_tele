from typing import List
from langchain_core.messages import BaseMessage
from db import pg_async_session
from sqlalchemy import select, func

from db.models import ConversationHistory


async def save_messages_to_db(
    user_id: int,
    message: BaseMessage,
    style: str | None = None,
    role_bot: str | None = None,
):
    async with pg_async_session() as db_session:
        new_record = ConversationHistory(
            user_id=user_id,
            role=message.type,
            style=style,
            role_bot=role_bot,
            content=message.content,
        )
        db_session.add(new_record)
        await db_session.commit()
        await db_session.close()


async def load_messages_from_db(user_id: int) -> List[BaseMessage]:
    async with pg_async_session() as db_session:
        statement = (
            select()
            .add_columns(ConversationHistory)
            .where(ConversationHistory.user_id == user_id)
        )
        result = await db_session.execute(statement)
        records = result.scalars().all()
        return records


async def clear_message_from_memory_bot(
    user_id: int, all: bool = False, first_record: ConversationHistory = None
) -> bool:
    """Удаляет сообщения из базы данных"""

    async with pg_async_session() as db_session:
        if not all and first_record:
            await db_session.delete(first_record)
            await db_session.commit()
            return True
        else:
            statement = ConversationHistory.__table__.delete().where(
                ConversationHistory.user_id == user_id
            )
            await db_session.execute(statement)
            await db_session.commit()
            return True
