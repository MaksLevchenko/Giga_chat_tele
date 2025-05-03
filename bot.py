from business_bot.handlers import (
    chat_handlers,
    other_handlers,
)
from business_bot.config.config import load_config
import asyncio
from aiogram import Bot, Dispatcher


config = load_config()
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = config.tg_bot.token


async def main():

    # Создаем объекты бота и диспетчера
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(chat_handlers.router)

    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# Запускаем поллинг
if __name__ == "__main__":
    asyncio.run(main())
