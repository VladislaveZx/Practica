from aiogram import Dispatcher, Bot
# from aiogram import parse mode html

from .local_settings import API_TOKEN
from .database.models import async_main
    
print()
dp = Dispatcher()

async def main():
    await async_main()
    
    bot = Bot(token=API_TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)
