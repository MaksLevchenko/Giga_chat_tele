from business_bot.handlers import (
    chat_handlers,
    other_handlers,
    style_handlers,
)
from keyboards import set_main_menu
from config.settings import settings
import asyncio
from aiogram import Bot, Dispatcher


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = settings.bot_token


async def main():

    # Создаем объекты бота и диспетчера
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(other_handlers.router)
    dp.include_router(style_handlers.router)
    dp.include_router(chat_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# Запускаем поллинг
if __name__ == "__main__":
    asyncio.run(main())
