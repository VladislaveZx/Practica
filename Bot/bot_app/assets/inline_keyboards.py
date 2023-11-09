from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


rsreu_site_button = InlineKeyboardButton(text='Сайт РГРТУ', url='http://rsreu.ru/')
cdo_site_button = InlineKeyboardButton(text='Сайт CDO', url='http://cdo.rsreu.ru/')
edu_site_button = InlineKeyboardButton(text='Сайт EDU', url='http://edu.rsreu.ru/')
menu_button = InlineKeyboardButton(text='В главное меню', callback_data='goto_menu')
