from aiogram import Dispatcher, Bot

from .local_settings import API_TOKEN

dp = Dispatcher()

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)
