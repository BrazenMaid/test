import asyncio
import logging
import nest_asyncio
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

nest_asyncio.apply()
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
USER_ID = int(os.getenv("TELEGRAM_USER_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    if message.from_user.id != USER_ID:
        return
    await message.answer("🤖 Киборг онлайн. Готов к управлению ботами.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling())
