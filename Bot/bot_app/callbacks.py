from typing import Any
from aiogram import types, Router
from aiogram.filters import Filter

from . import assets

from .app import dp

router = Router(name=__name__)

class MyFilter(Filter):
    def __init__(self, my_query: str) -> None:
        self.my_query = my_query
        
    async def __call__(self, query: types.CallbackQuery) -> bool:
        return query.data == self.my_query


@dp.callback_query(MyFilter(assets.inline_keyboards.menu_button.callback_data))
async def hello_message(query: types.CallbackQuery):
    from .messages import hello_message
    await hello_message(query.message)
