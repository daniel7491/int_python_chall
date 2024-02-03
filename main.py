import asyncio
import logging
import os
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    user_username = message.from_user.username
    await message.answer(f"Hi, {user_username}! Welcome to your bot!")


@dp.message()
async def message_catcher(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception as e:
        logging.error(f"Error sending message copy wrong file type: {e}")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
