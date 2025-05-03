from dataclasses import dataclass
import os
import dotenv


# dotenv.load_dotenv()


@dataclass
class TgBot:
    token: str


@dataclass
class GigaChat:
    secret_key: str


@dataclass
class Config:
    tg_bot: TgBot
    giga_key: GigaChat


def load_config() -> Config:
    dotenv.load_dotenv()
    return Config(
        tg_bot=TgBot(
            token=os.getenv("BOT_TOKEN"),
        ),
        giga_key=GigaChat(
            secret_key=os.getenv("GIGACHAT_KEY"),
        ),
    )


config = load_config()
