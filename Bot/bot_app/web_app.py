from aiogram import types, Router
from aiogram.filters import Filter

from . import assets

from .app import dp

router = Router(name=__name__)

class MyFilter(Filter):
    def __init__(self, check_data: str) -> None:
        self.check_data = check_data
        
    async def __call__(self, message: types.Message) -> bool:
        return message.web_app_data.button_text == self.check_data

@dp.message(MyFilter(check_data=assets.reply_keyboards.get_doc.text))
async def check_web_app_data(message: types.Message):
    import json
    data = json.loads(message.web_app_data.data)
    await message.answer(
        text=f'''
Получена новая заяка на:

Имя: {data['studname']}
Студенческий билет: №{data['studnum']}
Для {data['organisation']}

Ожидайте уведомление.
        '''
    )


