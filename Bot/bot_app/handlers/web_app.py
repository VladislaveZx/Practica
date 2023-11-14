from aiogram import types, Router
from aiogram.filters import Filter


# from .database.requests import add_request, create_stud
from ..database.requests import add_request, create_stud

from ..app import dp

router = Router(name=__name__)

class MyFilter(Filter):
    def __init__(self, check_data: str) -> None:
        self.check_data = check_data
        
    async def __call__(self, message: types.Message) -> bool:
        import json
        data = json.loads(message.web_app_data.data)
        print(data)
        return self.check_data == data['action']

@dp.message(MyFilter(check_data="document_request"))
async def document_request(message: types.Message):
    import json
    data = json.loads(message.web_app_data.data)
    flag = await add_request(
        user=message.from_user.id, 
        studnum=data['studnum'], 
        studname=data['studname'], 
        organisation=data['organisation']
    )
    if not flag:
        message_text = \
f'''
<b>Получена новая заяка на:</b>

Имя: {data['studname']}
Студенческий билет: №{data['studnum']}
Для {data['organisation']}

Ожидайте уведомление.
'''
    else:
        message_text = "Заяка уже есть"
    await message.answer(message_text)


@dp.message(MyFilter(check_data="reg_user"))
async def reg_user(message: types.Message):
    import json
    data = json.loads(message.web_app_data.data)
    print(data)
    # insert new user in db
    res = await create_stud(
        user=message.from_user.id,
        studnum=data['studnum'],
        studname=data['studname'],
        studgroup=data['studgroup'],
        studyear=data['studyear']
    )
    if not res:
        message_text = "Регистрация прошла успешно!"
    else: 
        message_text = "Вы уже зарегистрированы!"
    await message.answer(message_text)
        
    