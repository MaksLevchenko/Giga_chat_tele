from langchain_gigachat.chat_models import GigaChat

from config.settings import settings


GIGACHAT_KEY = (
    settings.gigachat_key
)  # Сюда нужно вставить Authorization key полученный у gigachat.
# Его можно получить вот здесь:
# https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-using-api#poluchenie-avtorizatsionnyh-dannyh

model = GigaChat(
    credentials=GIGACHAT_KEY,
    scope="GIGACHAT_API_PERS",
    model="GigaChat-2",
    streaming=False,
    verify_ssl_certs=False,
)
