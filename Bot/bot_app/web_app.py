from aiogram import types, Router
from aiogram.filters import Filter

from . import assets

from .app import dp

router = Router(name=__name__)

class MyFilter(Filter):
    def __init__(self, check_data: str) -> None:
        self.check_data = check_data
        
    async def __call__(self, message: types.Message) -> bool:
        import json
        data = json.loads(message.web_app_data.data)
        print(data)
        return self.check_data == data['action']

@dp.message(MyFilter(check_data="document_data"))
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


