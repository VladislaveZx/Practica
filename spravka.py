import telebot
from telebot import types

bot = telebot.TeleBot('6033027757:AAFvSKCpxAgC1DJice-KY9HZMqs3Z1xLBGY')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой ФВТ-бот! ")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('получить справку с места учебы')
        btn2 = types.KeyboardButton('Узнать расписание занятий')
        btn3 = types.KeyboardButton('Перейти на сайт РГРТУ')
        btn4 = types.KeyboardButton('Перейти на портал дистанционного обучения')
        btn5 = types.KeyboardButton('Перейти на портал образовательный портал РГРТУ')
        btn6 = types.KeyboardButton('Вернуться назад')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)



    elif message.text == 'получить справку с места учебы':
        pass




    elif message.text == 'Перейти на сайт РГРТУ':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Сайт РГРТУ', url='http://rsreu.ru/')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт РГРТУ", reply_markup = markup)




    elif message.text == 'Узнать расписание занятий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('245')
        btn2 = types.KeyboardButton('2415')
        btn3 = types.KeyboardButton('246')
        btn4 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "По кнопкам ниже можно узнать расписание занятий своей группы", reply_markup=markup)
    elif message.text == '245':
        f = open('245.jpg', 'rb')
        bot.send_photo(message.from_user.id, f)
    elif message.text == '2415':
        f = open('2415.jpg', 'rb')
        bot.send_photo(message.from_user.id, f)
    elif message.text == '246':
        f = open('', 'rb')
        bot.send_photo(message.from_user.id, f)
    elif message.text == 'Вернуться  в главное меню':
        pass



    elif message.text == 'Перейти на портал дистанционного обучения':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Сайт ЦДО', url='https://cdo.rsreu.ru/')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт ЦДО", reply_markup=markup)



    elif message.text == 'Перейти на портал образовательный портал РГРТУ':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Сайт EDU', url='https://edu.rsreu.ru/')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на образовательный портал РГРТУ", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
