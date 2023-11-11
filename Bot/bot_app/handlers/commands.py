from aiogram.filters import Command
from aiogram import types

from ..app import dp


@dp.message(Command(commands='start'))
async def cmd_start(message: types.Message):
    from assets.reply_keyboards import keyboard, hello_button
    from assets.message_text import send_hello
    
    markup = keyboard(buttons=[hello_button])
    message.answer(text=send_hello, reply_markup=markup)
    
    return
