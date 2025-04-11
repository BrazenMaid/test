
import asyncio
import os
import nest_asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

nest_asyncio.apply()
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
USER_ID = int(os.getenv("TELEGRAM_USER_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id != USER_ID:
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("Нажми", callback_data="test"))
    await message.answer("Привет! Тестовая кнопка:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data == "test")
async def test_button(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != USER_ID:
        return await callback_query.answer("Доступ запрещён", show_alert=True)
    await callback_query.answer("Кнопка работает!")
