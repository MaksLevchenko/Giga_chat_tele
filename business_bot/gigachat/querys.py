from langchain_core.messages import HumanMessage, SystemMessage
from .models import model


def get_gpt_response(news_text: str):
    """Обращается к gigachat и возвращает проанализированную новость"""
    messages = [SystemMessage(content="Имитируй обычное человеческое общение.")]
    messages.append(HumanMessage(content=news_text))
    res = model.invoke(messages)
    messages.append(res)
    return res.content
