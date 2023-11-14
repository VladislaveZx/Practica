from aiogram import types, Router
from aiogram.filters import Filter

from .. import assets

from ..app import dp

router = Router(name=__name__)

class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text
        
    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.my_text


# Hello message
@dp.message(MyFilter(assets.reply_keyboards.hello_button.text))
async def hello_message(message: types.Message):
    from ..assets.reply_keyboards import menu_buttons
    from ..assets.message_text import send_question
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=menu_buttons,
        resize_keyboard=True
    )
    await message.answer(text=send_question, reply_markup=keyboard)
    
    return


@dp.message(MyFilter(assets.reply_keyboards.back_button.text))
async def back_button(message: types.Message):
    await hello_message(message)


# Get ling to rsreu site
@dp.message(MyFilter(assets.reply_keyboards.rsreu_site.text))
async def get_doc(message: types.Message):
    from ..assets.inline_keyboards import menu_button, rsreu_site_button
    from ..assets.message_text import link_to_rsreu
    
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [rsreu_site_button],
            [menu_button]
        ]
    )
    await message.answer(text=link_to_rsreu, reply_markup=keyboard)
    
    return


# Get ling to cdo site
@dp.message(MyFilter(assets.reply_keyboards.cdo_site.text))
async def get_doc(message: types.Message):
    from ..assets.inline_keyboards import menu_button, cdo_site_button
    from ..assets.message_text import link_to_cdo
    
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [cdo_site_button],
            [menu_button]
        ]
    )
    await message.answer(text=link_to_cdo, reply_markup=keyboard)
    
    return


# Get ling to edu site
@dp.message(MyFilter(assets.reply_keyboards.edu_site.text))
async def get_doc(message: types.Message):
    from ..assets.inline_keyboards import menu_button, edu_site_button
    from ..assets.message_text import link_to_edu
    
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [edu_site_button],
            [menu_button]
        ]
    )
    await message.answer(text=link_to_edu, reply_markup=keyboard)
    
    return
