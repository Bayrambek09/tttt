import asyncio
import logging
import sys
from aiogram import Bot,Dispatcher,html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_KOKEN as token
bot=Bot(token=token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp=Dispatcher()

@dp.message(Command('start'))
async def CommandStart(message: Message):
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!")


@dp.message((F.from_user.id== 1958992995) & (F.text.contains ("admin") ))
async def vcx(message:Message):
   await message.answer(text="assalomu alaykum")









async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")