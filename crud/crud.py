from typing import List
from langchain_core.messages import BaseMessage
from db import pg_async_session
from sqlalchemy import select

from db.models import ConversationHistory


async def save_messages_to_db(user_id: int, messages: List[BaseMessage]):
    async with pg_async_session() as db_session:
        for msg in messages:
            new_record = ConversationHistory(
                user_id=user_id,
                role=msg.type,  # Преобразование type в строку
                content=msg.content,
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
        return [{"type": record.role, "content": record.content} for record in records]
