from aiogram import F, Router
import App.database as db
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import App.keyboards as kb
from aiogram.fsm.state import StatesGroup, State


router = Router()


# class Report():
#     reporter_id = State()
#     text = State()
#     date = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await db.db_start()
    await db.cmd_start_db(message.from_user.id)
    await message.answer("Привет!", reply_markup=kb.main)
