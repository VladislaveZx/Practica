from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


hello_button = KeyboardButton(text="👋 Поздороваться")


def menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton('получить справку с места учебы'),
        KeyboardButton('Узнать расписание занятий'),
        KeyboardButton('Перейти на сайт РГРТУ'),
        KeyboardButton('Перейти на портал дистанционного обучения'),
        KeyboardButton('Перейти на портал образовательный портал РГРТУ'),
        KeyboardButton('Вернуться назад')
    )
    return keyboard


def rsreu_site():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Сайт РГРТУ', url='http://rsreu.ru/')
    markup.add(btn1)
    return markup


def students_graph():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('245')
    btn2 = KeyboardButton('2415')
    btn3 = KeyboardButton('246')
    btn4 = KeyboardButton('Вернуться в главное меню')
    markup.add(btn1, btn2, btn3, btn4)
    return markup


def text_in_reply_keyboard(
    keyboard: ReplyKeyboardMarkup,
    text: str
):
    for string in keyboard.keyboard:
        for key in string:
            if text in key.values():
                return True
    return False
