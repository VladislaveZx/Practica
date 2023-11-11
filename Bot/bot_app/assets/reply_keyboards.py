from aiogram.types import WebAppInfo

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


hello_button = KeyboardButton(text="👋 Поздороваться")

site = KeyboardButton(text='Перейти в WebApp', web_app=WebAppInfo(url='https://iamlukovkin.github.io/Practica/'))
rsreu_site = KeyboardButton(text='Перейти на сайт РГРТУ')
cdo_site = KeyboardButton(text='Перейти на портал дистанционного обучения')
edu_site = KeyboardButton(text='Перейти на портал образовательный портал РГРТУ')
back_button = KeyboardButton(text='Вернуться назад')

menu_buttons = [
    [site], 
    [rsreu_site], 
    [cdo_site, edu_site], 
    [back_button]
]
    