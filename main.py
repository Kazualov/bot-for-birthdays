import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
# from handlers import start, tasks
import commands 


async def main():
    # Создаем экземпляры
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Регистрируем хендлеры
    dp.include_router(commands.router)

    # Запуск бота
    print("🤖 Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
