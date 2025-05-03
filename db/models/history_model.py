from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime

from db import Base


class ConversationHistory(Base):
    __tablename__ = "conversation_history"

    user_id = Column(Integer, nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
