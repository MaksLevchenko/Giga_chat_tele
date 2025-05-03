import asyncio
from pathlib import Path
import sys

from pydantic import model_validator, PostgresDsn

from pydantic_settings import BaseSettings, SettingsConfigDict

# Устанавливаем нужную политику событий для Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Settings(BaseSettings):
    # Конфигурация модели
    model_config = SettingsConfigDict(
        env_file="./.env",  # Файл с переменными окружения
        extra="ignore",  # Игнорируем лишние значения в env файле
    )

    # Телеграм
    bot_token: str | None = None

    # Giga_chat
    gigachat_key: str | None = None

    # Postgres
    pg_scheme: str = "postgresql+psycopg"
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_db: str | None = None
    pg_user: str | None = None
    pg_password: str | None = None

    pg_engine_echo: bool = False  # # Вывод сгенерированных запросов в логи

    postgres_url: str | None = None

    @model_validator(mode="after")
    def setting_validator(self) -> "Settings":
        file_version = ".version"
        if Path(file_version).exists():
            with open(file_version, "r") as fp:
                self.app_version = fp.readline()

        if not self.postgres_url:
            self.postgres_url = str(
                PostgresDsn.build(
                    scheme=self.pg_scheme,
                    username=self.pg_user,
                    password=self.pg_password,
                    # host=self.pg_host,
                    host="database",
                    port=self.pg_port,
                    path=self.pg_db,
                )
            )

        return self


settings = Settings()
