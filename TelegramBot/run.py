import asyncio
import config
import logging
from aiogram import Bot, Dispatcher
from App.handlers import router


bot = Bot(token=config.TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

# @dp.message(Command("get_photo"))
# async def get_photo:
#     await message.answer()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")