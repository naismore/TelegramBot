import asyncio
import config
import logging
from aiogram import Bot, Dispatcher
import App.database as db
from App.handlers import router


bot = Bot(token=config.TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")