import asyncio
import logging

from aiogram import Bot, Dispatcher, types


BOT_TOKEN = "6316810679:AAHvpaemNAPnLex1E5uDxoGvIp-BWDD5wn4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(message: types.Message):
    await message.answer(text=message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
