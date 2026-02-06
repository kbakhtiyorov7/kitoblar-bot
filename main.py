from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from buttons import (start_button)
import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message:Message):
    await message.answer("""Sizning obunangiz qayta yoqildi!

Obunani to'xtatish uchun /off buyrug'idan foydalaning.""")
    
    await message.answer("Bot yaratishni istaysizmi?\n"
                            "Marhamat, @Manybot saytimizga kiring.", reply_markup=start_button)




async def main():
  await  dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())