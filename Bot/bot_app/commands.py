from aiogram.filters import Command
from aiogram import types

from . import assets

from .app import dp


@dp.message(Command(commands='start'))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[assets.reply_keyboards.hello_button]],
        resize_keyboard=True
    )
    message_text = assets.message_text.send_hello
    
    await message.answer(text=message_text, reply_markup=keyboard)
    print(message.web_app_data)
    
    return