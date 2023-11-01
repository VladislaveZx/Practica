import telebot

from .. import config
from .. import assets


keyboards = assets.reply_keyboards
messages = config.settings.get_messages()
bot = config.settings.get_bot()
groups = ['245', '246', '2415']


def _hello_message(message: telebot.types.Message):
    user = message.chat.id
    keyboard = keyboards.menu_keyboard()
    reply_text = messages['have_question']
    bot.send_message(chat_id=user, text=reply_text, reply_markup=keyboard)
    return


def _rsreu_site(message: telebot.types.Message):
    user = message.chat.id
    keyboard = assets.reply_keyboards.rsreu_site()
    reply_text = "По кнопке ниже можно перейти на сайт РГРТУ"
    bot.send_message(chat_id=user, text=reply_text, reply_markup=keyboard)


def _graph(message: telebot.types.Message):
    user = message.chat.id
    keyboard = assets.reply_keyboards.students_graph()
    reply_text = "По кнопкам ниже можно узнать расписание занятий своей группы"
    bot.send_message(
        chat_id=user, 
        text=reply_text,
        reply_markup=keyboard
)
    

def _send_image(message: telebot.types.Message):
    user = message.chat.id
    image_name = message.text
    try:
        file = open(f'Bot/images/{image_name}.jpg', 'rb')
        bot.send_photo(user=user, photo=file)
    except Exception:
        bot.send_message(
            chat_id=user,
            text='На данный момент расписание для этой группы недоступно'
        )
        

def _cdo(message: telebot.types.Message):
    user = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='Сайт ЦДО', url='https://cdo.rsreu.ru/')
    markup.add(btn1)
    bot.send_message(
        chat_id=user, 
        text="По кнопке ниже можно перейти на сайт ЦДО", 
        reply_markup=markup
    )


def _edu(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='Сайт EDU', url='https://edu.rsreu.ru/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на образовательный портал РГРТУ", reply_markup=markup)


def registration():
    bot.register_message_handler(
        callback=_hello_message,
        func=lambda message: assets.reply_keyboards.text_in_reply_keyboard(
            keyboard=assets.reply_keyboards.hello_button,
            text=message.text
        )
    )
    bot.register_message_handler(
        callback=_hello_message,
        func=lambda message: message.text == 'Вернуться  в главное меню'
    )
    bot.register_message_handler(
        callback=_rsreu_site,
        func=lambda message: message.text == 'Перейти на сайт РГРТУ'
    )
    bot.register_message_handler(
        callback=_graph,
        func=lambda message: message.text == 'Узнать расписание занятий'
    )
    bot.register_message_handler(
        callback=_send_image,
        func=lambda message: message.text in groups
    )
    bot.register_message_handler(
        callback=_cdo,
        func=lambda message: message.text == 'Перейти на портал дистанционного обучения'
    )
    bot.register_message_handler(
        callback=_edu,
        func=lambda message: message.text == 'Перейти на портал образовательный портал РГРТУ'
    )
    return
